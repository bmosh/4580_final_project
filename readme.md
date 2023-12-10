4580 Final Project (FA23):

Simulating gender-based bias in the workplace:

The aim of the project is to use simulation modeling to study gender disparities in corporations,
and to perform counterfactual studies to understand how this can be remedied.

The model for the corporate form as implemented in the base simulation is as follows:

- The employees are classified into four levels: executives (E), senior-management (S),
management (M) and junior employees (J). The model takes as input a variable target num-
ber of employees at each level, which is customizable to allow for examination of the model
as it applies to businesses both large and small

- Each employee in level i ∈ {E, S, M, J} independently retires/leaves the company after
some Exp(λ + K) time, where λ is the mean gender stay time, and K is the mean level stay time. 
Note that λ+K acts as a **MEAN** parameter. The rate of departures are **LOWER** at higher levels (so K_E ≥
K_S ≥ K_M ≥ K_J ), as we believe there is more churn at lower levels, and senior level employees are more 
likely to remain at the company for longer. This value is RESET every time an employee is promoted, as their
happiness with the company is boosted following their promotion.

- The mean gender-staying time λ is a gender specific component;
in particular, there is evidence that women drop out faster than men (in particular, at
junior levels) due to childbirth and familial commitments. We chose to model this by saying
a woman at level L has an lower mean parameter λ for remaining with the company, and therefore is
more likely to exit the company at a sooner time.

- When an executive-level employee retires/leaves, the vacant position is filled by promot-
ing some chosen senior-manager. Similarly, any vacancy created at a lower level either
due to a promotion or a departure is immediately filled by promoting an employee from
the lower level. 

- There are several promotion schemes that we test to attempt mitigation of 
disproportionate gender distribution, including promoting based on the most senior employee option,
promoting based on a logit-combination of time-on-level and gender, and promoting based on a logit 
function of worker productivity.

- Junior-level vacancies are filled by immediately hiring ne.w employees, under the assumption that
there is an infinite pool of such potential hires

- We also test out the impact of maternity-leave within a company, in some trials giving women a small likelihood 
of being placed on leave for familial reasons, depending on their listed age. These slots are left unfilled until their return w.p. .49, (distributed from 
2 months to 2 years), or their leaving of the company w.p. .51.



The project file structure is as follows:

- FP_v1 ... FP_v4 are the WIP files from different stages of our project's development:
    - FP_v1 contains the original simulation code. This code is rudimentary and only supports a worker class
    and a simple hiring/promoting/leaving scheme.
    - FP_v2 adds in a simulation class that vastly improves the testing process- Now, we are able to pass-in
    various hiring/promoting/leaving schemes as we'd like, and automatically output PyPlot visualizations of
    the gender distributions at trial's end.
    - FP_v3 builds on v2, adding in the ability to run many repeated trials, while saving relevant information 
    to a CSV for further analysis. 
    - FP_v4 is the final main feature improvement stage, adding in maternity leave and vastly simplifying the
    process of selecting which kind of trial is to be run for creating large datasets.

- FP_Demo is a beautified version of FP_v4, retaining the key features of the simulation while splitting up
the simulation and worker classes into their own python files (simulation.py, worker.py), which was further 
optimized to remove redundancies and improve overall performance. It also features more detailed and readable
graphs to summarize gender distribution info.


