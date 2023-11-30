4580 Final Project (FA23):

Simulating gender-based bias in the workplace:

The aim of the project is to use simulation modeling to study gender disparities in corporations,
and to perform counterfactual studies to understand how this can be remedied.

The model for the corporate form as implemented in the base simulation is as follows:

- The employees are classified into four levels: executives (E), senior-management (S),
management (M) and junior employees (J). The model takes as input some target num-
ber of employees at each level (for example, it could be 5, 20, 100 and 400 respectively),
which is decided by some external reasons (budget, need, etc.).

- Each employee in level i ∈ {E, S, M, J} independently retires/leaves the company after
some Exp(λL) time. The rate of departures may be higher at higher levels (so λE ≥
λS ≥ λM ≥ λJ ) if you believe older people retire sooner, or the opposite if you believe
there is more churn at lower levels (you could study both to see which is worse).

- The rate of people dropping out of the workforce also has a gender specific component;
in particular, there is evidence that women drop out faster than men (in particular, at
junior levels) due to childbirth and familial commitments. You can model this by saying
a woman at level L has an additional timer Exp(κL), and exits the company at the
minimum of the two timers (which is equivalent to saying that each woman in level L
exits after Exp($\lambda$ + $\lambda$ + $\lambda$L) time.

- When an executive-level employee retires/leaves, the vacant position is filled by promot-
ing some chosen senior-manager. Similarly, any vacancy created at a lower level either
due to a promotion or a departure is immediately filled by promoting an employee from
the lower level. Finally, junior-level vacancies are filled by hiring new employees (assume
there is an infinite pool of such potential hires)

From here, a variety of hiring, promotion, and leaving scenario simulations were tested. (WE ARE HERE)

- Think of new ways to promote equality in the workplace and test them out to see their impact.
