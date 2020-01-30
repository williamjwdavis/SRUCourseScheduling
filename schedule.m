nclasses=8; %number of classes, with sections of a course counting as distinct classes 
ngroups=6; %number of groups of courses, with sections of a course counting as the same class
nprofs=4; %number of professors
ntimes=9; %number of time slots, numbered horizontally accross days 1,2,3; 4,5,6; 7,8,9
nrooms=2; %number of classrooms

%x variables are x_{ijkl}, where i is classes, j is profs, k is times, l is rooms
%x_{ijkl}=1 if class i is taught by prof j at time k in room l, and 0 otherwise
%y variables are auxiliary and come after x, y_{gj} where g is goup of classes and j is profs

%nx is number of x variables
nx=nclasses*nprofs*ntimes*nrooms;

%ny is number of y variables
ny=nprofs*ngroups;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%EQUALITY CONSTRAINTS%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%initialize equality constraint matrix and initialize row counter
Aeq=sparse(zeros(1,nx+ny));
beq =[0];
currentRow = 1;



%The next 6 sets of constraints represent forbidden pairs from the sets
%"classes", "faculty", "times", "rooms". They each have the form:
%sum_{each pair of forbidden two indices, all pairs of other two indices} x_{i,j,k,l} = 0 

%An equivalent formulation is:
%sum_{all pairs of other two indices} x_{i,j,k,l} = 0 for each pair of forbidden two indices

%Another equivalent formulation is: 
%x_{i,j,k,l}=0 for each pair of forbidden indices and all pairs of other two indices

%The third formulation has the most constraints, but they are the simplest (just one nonzero entry). 
%The second formulation has fewer constraints, but they more complicated (i.e., having more nonzero entries). 
%The first formulation has the fewest constraints (just one), but also the most complicated constraints (i.e., having the most nonzeros). 

%To convert between the first formulation and the second, move the lines
%beq(currentRow) = 0;
%currentRow = currentRow + 1;
%between the second and third "end" in each set of constraints

%To convert to the third formulation, move the lines
%beq(currentRow) = 0;
%currentRow = currentRow + 1;
%between "Aeq(currentRow, f(i,j,k,l)) = 1;" and the first "end"

%It's not obvious which option is better; maybe some computational tests should be run to find out.

%unsuitable rooms for course i
forbidden_rooms_for_course={[],[],[2],[2],[1],[1],[],[2]};

for i=1:nclasses
    for l=forbidden_rooms_for_course{i}
        for j = 1:nprofs
            for k = 1:ntimes
                Aeq(currentRow, f(i,j,k,l)) = 1;
            end
        end
    end
end
beq(currentRow) = 0;
currentRow = currentRow + 1;

%unavailable time slots for room l
forbidden_times_for_room={[],[]};

for l=1:nrooms
    for k=forbidden_times_for_room{l}
        for i = 1:nclasses
            for j = 1:nprofs
                Aeq(currentRow, f(i,j,k,l)) = 1;
            end
        end
    end
end
beq(currentRow) = 0;
currentRow = currentRow + 1;

%unsuitable times for course i
forbidden_times_for_class={[],[7 8 9],[1 2 3],[1 2 3],[],[],[1 3 4 6 7 9],[1 4 7]};

for i=1:nclasses
    for k=forbidden_times_for_class{i}
        for j = 1:nprofs
            for l = 1:nrooms
                Aeq(currentRow, f(i,j,k,l)) = 1;
            end
        end
    end
end
beq(currentRow) = 0;
currentRow = currentRow + 1;

%unsuitable times for faculty j
forbidden_times_for_faculty={[1 2 3],[2 5 8],[7 8 9],[]};

for j=1:nprofs
    for k=forbidden_times_for_faculty{j}
        for i= 1:nclasses
            for l = 1:nrooms
                Aeq(currentRow, f(i,j,k,l)) = 1;
            end
        end
    end
end
beq(currentRow) = 0;
currentRow = currentRow + 1;

%unsuitable courses for faculty j
forbidden_class_for_faculty={[],[7],[],[2]};

for j=1:nprofs
    for i=forbidden_class_for_faculty{j}
        for k = 1:ntimes
            for l = 1:nrooms
                Aeq(currentRow, f(i,j,k,l)) = 1;
            end
        end
    end
end
beq(currentRow) = 0;
currentRow = currentRow + 1;
        
    
%unsuitable rooms for faculty j
forbidden_rooms_for_faculty={[],[],[],[]};

for j=1:nprofs
    for l=forbidden_rooms_for_faculty{j}
        for k = 1:ntimes
            for i = 1:nclasses
                Aeq(currentRow, f(i,j,k,l)) = 1;
            end
        end
    end
end
beq(currentRow) = 0;
currentRow = currentRow + 1;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%c(i) is number of credits of class i
c=[3 3 2 2 3 3 1 1];


%To require a certain room for a course, simply forbid all other rooms.

%To require a time for a course, simply forbid all other times.

%To require a faculty for a course (i.e., to say faculty j must teach course i), we use the constraints: 
%sum_{k,l} x_{i,j,k,l}=c(i) for each required pair i,j
%this means the number of times i,j appears in the schedule (over all rooms and time slots) is c(i). 
%This is sufficient, since it is later enforced that class i appears in exactly c(i) time slots.

%This constraint could also be restructured as 
%sum_{k,l} x_{i,j,k,l}\geq 1 for each required pair i,j. 
%This is sufficient since later it is enforced that each course is taught by exactly one professor. 

%The constraint could also be restructured as 
%for each required pair (I,J), x_{Ijkl}=0 for all k,l, and all j!=J
%Or, summing, sum_{j!=J,k,l} x_{I,j,k,l}=0 for each required pair (I,J). 
%These can be applied to enforcing a required room for a course and required time for a course, as well.

%It's not obvious which option is better; maybe some computational tests should be run to find out.

required_courses_faculty={[],[],[],[1]};

for j=1:nprofs
    for i=required_courses_faculty{j}

        for k = 1:ntimes
            for l = 1:nrooms
                Aeq(currentRow, f(i,j,k,l)) = 1;
            end
        end
        beq(currentRow) = c(i);
        currentRow = currentRow + 1;        

    end
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%class i appears c(i) times on the schedule
%If each time slot corresponds to one credit hour, then this set of constraints 
%enforces the requirement that that each class is taught for c(i) credit hours. 
%If Tuesday/Thursday days are added with longer classes (e.g. 90 minutes each, 
%counting for 1.5 credit hours) then this set of constraints will have to change.
%The constraints now are simply enforced as 
%sum_{j,k,l} x_{i,j,k,l}=c(i) for each i


for i=1:nclasses
    for j = 1:nprofs
        for k=1:ntimes
            for l = 1:nrooms
                Aeq(currentRow, f(i,j,k,l)) = 1;
            end
        end
    end
    beq(currentRow) = c(i);         %recall c(i) is the number of credits of class i
    currentRow = currentRow + 1;
end




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
%%%%%%INEQUALITY CONSTRAINTS%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%initializing inequality matrix and re-initializing row count
A=sparse(zeros(1,nx+ny));
b =[0];
currentRow = 1;

%class is at same time every day

forbidden_pairs={[1 5],[1 8],[1 6],[1 9],[2 4],[2 7],[2 6],[2 9],[3 4],[3 7],[3 5],[3 8],[4 8],[4 9],[5 7],[5 9],[6 7],[6 8]};

for i=1:nclasses
    for t=1:length(forbidden_pairs)
        temp=forbidden_pairs{t};
        for j = 1:nprofs
            for l = 1:nrooms
                A(currentRow, f(i,j,temp(1),l)) = 1;
                A(currentRow, f(i,j,temp(2),l)) = 1;
            end   
        end   
        b(currentRow) = 1;
        currentRow = currentRow + 1;   
    end
end

%class is in the same room every day


forbidden_pairs_room={[1 2]};

for i=1:nclasses
    for t=1:length(forbidden_pairs_room)
        temp=forbidden_pairs_room{t};

        for j1 = 1:nprofs
            for k1 = 1:ntimes
                for j2 = 1:nprofs
                    for k2 = 1:ntimes
                        A(currentRow, f(i,j1,k1,temp(1))) = 1;
                        A(currentRow, f(i,j2,k2,temp(2))) = 1;
                        b(currentRow) = 1;
                        currentRow = currentRow + 1;   
                    end
                end
            end   
        end   

    end
end






%class is taught by same prof every day
%%%%%%%%%%%%%%%%%%%%%%%%FINISH
forbidden_pairs_prof={[1 2],[1,3],[1,4],[2,3],[2,4],[3,4]};

for i=1:nclasses
    for t=1:length(forbidden_pairs_prof)
        temp=forbidden_pairs_prof{t};

        for k1 = 1:ntimes
            for l1 = 1:nrooms
                for k2=1:ntimes
                    for l2=1:nrooms
                        
                        A(currentRow, f(i,temp(1),k1,l1)) = 1;
                        A(currentRow, f(i,temp(2),k2,l2)) = 1;
                        b(currentRow) = 1;
                        currentRow = currentRow + 1;   
        
                    end   
                end   
            end
        end
        
    end
end





%%%%The following pairs of classes cannot be taught simultaneously%%%
restricted_pairs_of_classes={[2,5], [2,6], [3,8], [4,8]};

%To ensure this, we use the following constraints: 
%sum_{j,l} x_{i,j,k,l} <= 1 for each time slot and each forbidden pair of classes
%This means that a forbidden pair of classes cannot appear in the schedule at the same time slot. 

for k = 1:ntimes
    for t=1:length(restricted_pairs_of_classes)
        temp=restricted_pairs_of_classes{t};
        for j = 1:nprofs
            for l = 1:nrooms
                A(currentRow, f(temp(1),j,k,l)) = 1;
                A(currentRow, f(temp(2),j,k,l)) = 1;
            end
        end
        b(currentRow) = 1;
        currentRow = currentRow + 1;
    end
end


%TEACHING LOAD

%load_upper(j) is upper bound on teaching load of faculty j
load_upper=[6 6 999 6];

%Assuming each time slot is one credit hour, we enforce the teaching load
%by assuring that prof j appears at most load_upper(j) times on the schedule.
%More precisely, for each j, sum_{1,k,l}x_{i,j,k,l} <= load_upper(j)
%If different time slots count for different numbers of credits, this will have to be amended

for j=1:nprofs

for i = 1:nclasses
    for k = 1:ntimes
        for l = 1:nrooms
            A(currentRow, f(i,j,k,l)) = 1;
        end
    end
end
b(currentRow) = load_upper(j);
currentRow = currentRow + 1;

end

%load_lower(j) is lower bound on teaching load of faculty j
load_lower=[0 0 3 0];

%Assuming each time slot is one credit hour, we enforce the teaching load
%by assuring that prof j appears at least load_lower(j) times on the schedule.
%More precisely, for each j, sum_{1,k,l}x_{i,j,k,l} => load_upper(j)
%If different time slots count for different numbers of credits, this will have to be amended

for j=1:nprofs

for i = 1:nclasses
    for k = 1:ntimes
        for l = 1:nrooms
            A(currentRow, f(i,j,k,l)) = -1;
        end
    end
end
b(currentRow) = -load_lower(j);
currentRow = currentRow + 1;

end





%DAILY SUMS OF CLASSES
%at most one time slot of each class per day

Monday=[1 4 7];
Wednesday=[2 5 8];
Friday=[3 6 9];
day={Monday, Wednesday, Friday};

for i=1:nclasses
    for d=1:3
        for j = 1:nprofs
            for k = day{d}
                for l = 1:nrooms
                    A(currentRow, f(i,j,k,l)) = 1;
               end
           end
        end
    b(currentRow) = 1;
    currentRow = currentRow + 1;
    end
end




%no two profs teach in the same room at the same time
%no two classes are taught in the same room at the same time
for k=1:ntimes
    for l=1:nrooms
        
        for i = 1:nclasses
            for j = 1:nprofs
                A(currentRow, f(i,j,k,l)) = 1;
            end
        end
        b(currentRow) = 1;
        currentRow = currentRow + 1;
        
    end
end


%no prof teaches in different rooms at the same time
%no prof teaches different classes at the same time


for k=1:ntimes
    for j=1:nprofs
 
        for i = 1:nclasses
            for l = 1:nrooms
                A(currentRow, f(i,j,k,l)) = 1;
            end
        end
        b(currentRow) = 1;
        currentRow = currentRow + 1;

    end
end




%number of preps

%groups of classes which are sections of the same course
groups={[1], [2], [3 4], [5 6], [7], [8]};

for j=1:nprofs
    for t=1:length(groups)
        temp=groups{t};
        for k=1:ntimes
            for l=1:nrooms
                for i=temp
                    A(currentRow, f(i,j,k,l)) = 1/(length(temp)*c(i));
                end
            end
        end
        A(currentRow, nx+g(t,j)) = -1;
        b(currentRow) = 0;
        currentRow = currentRow + 1;

        for k=1:ntimes
            for l=1:nrooms
                for i=temp
                    A(currentRow, f(i,j,k,l)) = -1/(length(temp)*c(i));
                end
            end
        end
        A(currentRow, nx+g(t,j)) = 1; 
        b(currentRow) = 0.999;
        currentRow = currentRow + 1;
    end
end
    
    
    



max_preps=[1 1 2 3];
for j = 1:nprofs
    for t=1:length(groups)
        A(currentRow, nx+g(t,j)) = 1;
    end
    b(currentRow) = max_preps(j);
    currentRow = currentRow + 1;
end



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
%%%%%% BUILD MODEL AND SOLVE %%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%objective function is just constant. If there is no feasible solution, some objective can be 
%introduced, e.g., relax some constraints and maximize the number of them that are satisfied
[z,fval]=intlinprog(ones(nx+ny,1),1:nx+ny,A,b,Aeq,beq,zeros(nx+ny,1),ones(nx+ny,1));

%only interested in x variables, which occupy the first nx positions of the solution vector
z=z(1:nx);

%get the positions of the nonzero entries of the solution 
nonzero_z=find(z);

%output the ordered quadruples corresponding to these positions (according to the function finv)
for i=1:length(nonzero_z)
finv(nonzero_z(i))
end

