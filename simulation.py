import numpy as np
import time
import worker as wr
import matplotlib.pyplot as plt

class Simulation(object):
    """
    A class to streamline the simulation process. 
    """
    
    def __init__(self, sim_type, level_sizes, leaving_process, \
                 hiring_process, promotion_process, alpha, gamma, male_productivity, female_productivity, parental_leave=False,
                 round_length=10, num_rounds=6):
        
        self.work_levels = work_levels = {
            1 : "J",
            2 : "M",
            3 : "S",
            4 : "E"
        }
        self.worker_db = {
            1 : [],
            2 : [],
            3 : [],
            4 : []
        }
        self.leave_db = {
            1 : [],
            2 : [],
            3 : [],
            4 : []
        }

        self.male_round_gender_dists = [
            [],
            [],
            [],
            []
        ]

        self.female_round_gender_dists = [
            [],
            [],
            [],
            []
        ]

        self.sim_type = sim_type
        self.level_sizes = level_sizes
        
        self.leaving_process = leaving_process
        self.hiring_process = hiring_process
        self.promotion_process = promotion_process

        self.alpha = alpha
        self.gamma = gamma

        self.male_productivity = male_productivity
        self.female_productivity = female_productivity
        
        self.round_length = round_length
        self.num_rounds = num_rounds
        
        self.parental_leave = parental_leave
        self.worker_idx = 1
                
    def hire_workers(self, all_male = False, all_female = False, pt = False):
        level = max(self.worker_db.keys())
        
        while level >= 1:
            while len(self.worker_db[level]) + len(self.leave_db[level]) < self.level_sizes[level]:
                self.hiring_process(self.worker_db, level, self.worker_idx,\
                                     self.male_productivity, self.female_productivity, \
                                        all_male, all_female)
                self.worker_idx += 1
                if pt:
                    print("Hire made at level: ", level)
            level -= 1

    def level_gender_distribution(self, worker_level):
        count_male = 0
        count_female = 0
        total = 0

        for wrkr in worker_level:
            if wrkr.is_male():
                count_male += 1
            else:
                count_female += 1
            total += 1

        pct_male = count_male/total
        pct_female = count_female/total
        
        return pct_male, pct_female
    
    def print_final_demo_info(self):
        for level in self.worker_db.keys():
            print("Population Demographics for level %s of size %i:" % (self.work_levels[level], self.level_sizes[level]))
            print("population pct. male: %f, population pct. female: %f\n" % (self.level_gender_distribution(self.worker_db[level])))

    def print_gender_distribution(self):
        count_male = 0
        count_female = 0
        total = 0

        for level in self.worker_db.keys():
            for wrkr in self.worker_db[level]:
                if wrkr.is_male():
                    count_male += 1
                else:
                    count_female += 1
                total += 1

        print("population male: %i, population female: %i, total: %i \n" % (count_male, count_female, total))
            
    def visualize_final_level_gender_dists(self):
        for level in range(1,5):
            plt.figure()
            ax = plt.gca()
            ax.set_ylim(0, 1)
            ax.set_xlim(-1, self.num_rounds+1)
            plt.title("Percentage Male Workers for Level %s Over Simulation Rounds" % self.work_levels[level])
            plt.xlabel("Round Number")
            plt.xticks([i for i in range(0, self.num_rounds+1)], fontsize="xx-small")
            plt.ylabel("Worker Proportion By Gender")
            plt.bar([i for i in range(self.num_rounds+1)], self.male_round_gender_dists[level-1], color="deepskyblue")
            plt.bar([i for i in range(self.num_rounds+1)], self.female_round_gender_dists[level-1], bottom=self.male_round_gender_dists[level-1], color="pink")
            plt.plot([i for i in range(-1, self.num_rounds+2)],[.5 for i in range(-1, self.num_rounds+2)], label="50% proportion men/women",color="black")
            plt.plot([i for i in range(-1, self.num_rounds+2)], [np.mean(self.male_round_gender_dists[level-1]) \
                                                                 for i in range(-1, self.num_rounds+2)], color="white", label="mean proportion of men in level")
            plt.legend(loc="lower left")
            plt.show()
    
    def update_workforce(self, alpha, gamma):
        # Delete expired workers:
        self.leaving_process(self.worker_db)
        
        if self.parental_leave:
            self.base_check_leave(self.worker_db, self.leave_db)
        else:
            for level in self.leave_db.keys():
                assert len(self.leave_db[level]) == 0
        
        for level in self.worker_db.keys():
            if self.sim_type == "base":
                self.worker_db[level].sort(key=wr.Worker.get_time_on_level, reverse=True)
            elif self.sim_type == "logit":
                self.worker_db[level].sort(key=wr.Worker.get_time_on_level, reverse=True)
            elif self.sim_type == "prod":
                self.worker_db[level].sort(key=wr.Worker.get_productivity, reverse=True)
            else:
                raise Exception("Check Sim Type!!!")
                
        
        # Promote to fill ranks:  
        self.promotion_process(self.worker_db,self.leave_db, alpha, gamma, pt=False, n=4)
        
        # Add new hires to fill out staff:
        self.hire_workers(pt=False)

    
    def run_simulation(self, prnt=False):
        
        self.hire_workers()
        
        for level in range(1,5):
                self.male_round_gender_dists[level-1].append(self.level_gender_distribution(self.worker_db[level])[0])
                self.female_round_gender_dists[level-1].append(self.level_gender_distribution(self.worker_db[level])[1]) 
        
        if prnt:
        
            print("Pre-Simulation Demographic Info:\n")

            print("Overall Gender Distribution:\n")
            self.print_gender_distribution()

            print("Level-Split Gender Distribution:\n")
            self.print_final_demo_info()

            print("Startng Simulation: %i rounds of %i seconds each." % (self.num_rounds, self.round_length))
        
        start_time = time.time()

        for i in range(self.num_rounds):
            if prnt:
                print("starting new round")
            # for duration of simulation length:
            while time.time() <= start_time + self.round_length:
                self.update_workforce(self.alpha, self.gamma)
                time.sleep(.05)
                if (time.time() - start_time) % (self.round_length/5) < .06: 
                    pct_complete = min(100,round(((time.time() - start_time) / self.round_length*100)))
                    if prnt:
                        print("round %i %i%s complete" % (i+1, pct_complete, "%"))
            if prnt:
                print("round complete.")
                self.print_gender_distribution()
            
            # Record Level Gender Distributions
            for level in range(1,5):
                self.male_round_gender_dists[level-1].append(self.level_gender_distribution(self.worker_db[level])[0]) 
                self.female_round_gender_dists[level-1].append(self.level_gender_distribution(self.worker_db[level])[1]) 

            start_time = time.time()
        
        
        if prnt:
            print("Simulation Complete. Final Stats:\n")
            self.print_final_demo_info()
            self.visualize_final_level_gender_dists()
        

        