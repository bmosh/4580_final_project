import numpy as np
import random
import time


# Worker Class:
class Worker(object):
    
    def __init__(self, level, gender, idx, start_time):
        self.level = level
        self.gender = gender
        self.idx = idx
        self.age = 12*level + random.randint(10,30)
        self.start_time = start_time
        
    def __str__(self):
        return "[level: %s, gender: %s, id: %i, end_time: %f]" \
            % (self.level, self.gender, self.idx, self.end_time)
        
    def get_index(self):
        return self.idx
    
    def get_level(self):
        return self.level
    
    def get_productivity(self):
        return self.productivity
    
    def set_productivity(self, male_productivity, female_productivity):
        if self.gender == 0:
            self.productivity = max(np.random.normal(male_productivity[0], male_productivity[1]), 1)
        else:
            self.productivity = max(np.random.normal(female_productivity[0], female_productivity[1]), 1)
    
    def get_time_on_level(self):
        return time.time() - self.start_time
    
    def get_end_time(self):
        return self.end_time
    
    def set_end_time(self, gender_stay_times, level_ext_stay_times):
        
#       Setting end time for male employees
        if self.gender == 0:
            self.end_time = self.start_time \
                + np.random.exponential( \
                gender_stay_times[self.gender] + level_ext_stay_times[self.level])
            
#       Setting end time for female employees - As of now, same as male but with lower mean, not 2 Expo RVs
        else:
            self.end_time = self.start_time \
                + np.random.exponential( \
                gender_stay_times[self.gender] + level_ext_stay_times[self.level])
    
    def det_go_on_leave(self):
        u = np.random.uniform()
        
        if self.get_gender() == 1:
            if self.age < 25:
                if u < .01:
                    self.set_leave_time()
                    return True
            elif self.age < 30:
                if u < .02:
                    self.set_leave_time()
                    return True
            elif self.age < 35:
                if u < .005:
                    self.set_leave_time()
                    return True
            elif self.age < 40:
                if u < .0025:
                    self.set_leave_time()
                    return True
            elif self.age < 45:
                if u < .0001:
                    self.set_leave_time()
                    return True
        
        return False
                
    def get_leave_time(self):
        return self.leave_time
    
    def set_leave_time(self):
        u = np.random.uniform()
        
        if u < .12:
            self.leave_time = time.time() + 1/6
        elif u < .49:
            self.leave_time = time.time() + (4/11*u + 124/11)/12
        else:
            self.leave_time = time.time()
            self.end_time = time.time()
    
    def is_male(self):
        return self.gender == 0
    
    def promote(self, gender_stay_times, level_ext_stay_times):
        self.level += 1
        self.start_time = time.time()
        self.set_end_time(gender_stay_times, level_ext_stay_times)