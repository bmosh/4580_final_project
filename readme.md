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

- Junior-level vacancies are filled by immediately hiring new employees, under the assumption that
there is an infinite pool of such potential hires

- We also test out the impact of maternity-leave within a company, in some trials giving women a small likelihood 
of being placed on leave for familial reasons, depending on their listed age. These slots are left unfilled until their return w.p. .49, (distributed from 
2 months to 2 years), or their leaving of the company w.p. .51.

