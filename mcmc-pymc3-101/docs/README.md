



# An introduction to Markov Chain Monte Carlo

WRITE BRIEF INTRODUCTION.

## Bayes' theorem

Bayes'  theorem states that the conditional probability of an event $A$ given event $B$ can be expressed by

$p(A|B) = \dfrac{p(A)p(B|A)}{p(B)}$.

Bayes' theorem can also be applied to parameter estimation, where the expression becomes

$p(\theta\, \vert\, X,y) = \dfrac{p(\theta) p(y\, \vert\, X,\theta)}{p(y \, \vert \,X)}$,

or 

$p(\theta\, \vert\,y) = \dfrac{p(\theta) p(y\, \vert\,\theta)}{p(y)}$, 

depending on the textbook you consult. We will use the latter notation for brevity. 

In the context of parameter estimation, the above equation is an expression that encapsulates how our beliefs about a (set of) parameter(s) $\theta$ changes after observing the data $(X,\, y)$. 

(Note the slight abuse of notation above: We use $p(\cdot)$ to denote the distributions of the posterior, prior, likelihood and marginal likelihood, but this does not necessarily mean that they share the same distribution.)

#### Priors, likelihoods and posteriors

Let's decode this expression, starting with the numerator on the right-hand side: 

The prior distribution of $\theta$ is denoted by $p(\theta)$. It expresses any beliefs or assumptions we might have about the parameter(s) prior to observing the data. Strong priors are more informative, meaning $p(\theta)$ is more concentrated around some values of $\theta$. On the other hand, having no particular beliefs about the parameters should result in a more uniform, or uninformative, prior.

Next is the likelihood $p(y\, \vert\, \theta)$. The likelihood is a model parameterised by $\theta$ which expresses the plausability of observing the data given some value of $\theta$.

In the denominator we have $p(y)$, also called the marginal likelihood, average likelihood, model evidence, etc. We will call it the average likelihood, because it can be expressed as an expectation:

$p(y) = \mathbb{E}_{\theta}[p(y\,\vert\,\theta)] = \int p(y\,\vert\,\theta)p(\theta)\,d\theta$. 

The average likelihood's job is to serve as a normalising constant, i.e. to ensure that the posterior distribution  $p(\theta \, \vert \, y)$​ integrates to 1. The posterior distribution is our updated belief about the parameter value(s) $\theta$ after observing the data $(X, y)$. 

Often you'll see the expression

$p(\theta \, \vert \, y) \propto p(\theta) p(y\, \vert\,\theta)$,

where the notation $\propto$ indicates that the posterior is proportional to the prior times the likelihood (i.e. it is unnormalised). In practice the average likelihood is often unknown or very difficult to obtain. Fortunately, it is not needed in Markov Chain Monte Carlo methods, as we will see later.

#### Posterior predictive distribution

After calculating the posterior distribution of the parameters, we can compute the likelihood of a new observation $x^*$ taking on a certain value $y^*$. This is called the posterior predictive distribution, given by

$p(y^* \, \vert \, y) = \int p( y^* \,\vert\, \theta) p(\theta \,\vert\, y) \,d\theta$.

The posterior predictive distribution can be viewed as an ensemble of models with different settings of $\theta$, weighted by posterior distribution $\theta$. Thus the most likely parameter values will contribute the most to the probability of $y^*$ taking on a particular value. 

Making statements about parameter values and predictions in terms of probability highlights one of the key features of the Bayesian approach: It gives an intuitive and principled way of expressing uncertainty.

MOTIVATE WHY WE NEED MCMC.



## Markov chains

Markov chains are used to model many interesting things, such as industrial manufacturing processes, social mobility, queuing systems, etc. Famously, Markov chains were instrumental in the development of Google's PageRank algorithm.

A Markov chain is a way of defining a joint probability distribution over sequences. Another interpretation of Markov chains is that they are dynamical stochastic systems, where we jump from one state to another at each time step. 

Markov chains can be used to model events in discrete and continuous time. Typically we are interested in the long-term distribution of being in a certain state.

In this section we will briefly cover the product rule of probability before giving a basic introduction to Markov chains. We spend some time discussing the stationary distribution, as it plays a central role in Markov chain Monte Carlo methods.

### The product rule

Any joint probability distribution can be written as the product of conditional distributions. Consider the following example of the joint probability distribution over the random variables $X_1, X_2, X_3$ and $X_4$:

$$P(X_1, X_2, X_3, X_4) = P(X_1)P(X_2\,|\,X_1)P(X_3\,|\,X_2, X_1)P(X_4\,|\,X_3, X_2, X_1)$$.

This is also known as the product rule (sometimes chain rule) of probability, which we will revisit shortly.

### Markov chain basics

A Markov chain typically models a sequence of observations $X_1, X_2,\ldots, X_T$ for some arbitrary $T$. The subscript $t \in T$ can for example denote a time step, but it can also denote the location within a sequence. From now on we simply refer to $t$ as the time step, and we assume that $t$ is discrete, i.e. $t \in \{1, \,\ldots, T\}$. 

The fundamental assumption of a Markov chain is that the present time step contains all the information we need to make predictions about the future:

$$P(X_t\,|\,X_{t-1}, X_{t-2}, \ldots, X_1) = P(X_t\,|\,X_{t-1})$$.

This is sometimes referred to as the memoryless property. The joint distribution of a sequence of $T$ events can thus be factorised according to the product rule, but this time incorporating the Markov property:

$$\begin{align*}P(X_1, X_2, \,\ldots, X_T) &= P(X_1)P(X_2\,|\,X_1)P(X_3\,|\,X_2)\,\ldots P(X_T \,|\, X_{t-1}) \\ &= P(X_1) \prod_{i=2}^{T}P(X_t\,|\,X_{t-1})\end{align*}$$

When the state-space of $X_t \in \{1, \,\ldots, K\}$  is discrete, we have what is called a finite-state Markov chain. We will limit ourselves to these types of models for simplicity.

### Visualising Markov chains

Consider a finite-state Markov chain with two states, i.e. $X_t \in \{1, 2\}$. This can be represented by the following graph:

 <img src="figs/simple_example.pdf" alt="simple_example.pdf" style="zoom:250%;" />

Each node is a state, and the directed edges connecting the nodes denote the probability of transitioning from one state to the next, or in some cases the probability of remaining in the current state (a self-loop).

These transition probabilities can be described by a $K \times K$ matrix $\mathbb{A}$ with rows indexed by $i$ and columns indexed by $j$. $\mathbb{A}$ Is called a transition matrix or a stochastic matrix, and $A_{ij}(t) = P(X_t=j\,|\,X_{t-1} = i)$ is the probability of transitioning from state $i$ to state $j$ at time $t$. If $\mathbb{A}$ is constant over time (i.e. $A_{ij}(t) = A_{ij}$ for all $t$), we call the Markov chain homogenous or time-invariant. We assume that our Markov chains are time-homogenenous for simplicity.

As an example, the transition matrix for the Markov chain above would be

$\mathbb{A} = \begin{bmatrix} 0.1 & 0.9 \\ 0.8 & 0.2 \end{bmatrix}$.

Note that the row probabilites are constrained to sum to 1, i.e. $\sum_{j} A_{ij} = 1$. 

### The stationary distribution

Often we are interested in the long-term distribution over states. For example, what is the long run probability of being in state 2 in the example above?

Generally, given some initial distribution $\pi_0 = [P(X_0 = 1), \ldots, P(X_0 = K)]$ describing the probability of starting in a particular state at time $t=0$, the probability distribution over states at time $t=1$ is given by

<span style="color: red;">(1)</span> $$\pi_1 = \pi_0 \mathbb{A}$$.

**Example:** Let's explicitly calculate $\pi_1$ for the chain in figure 1. First, we write out the problem in probability statements to make it completely clear what is happening:

$\pi_1 = [P(X_1 = 1), P(X_1 = 2)]$

$\pi_0 = [P(X_0 = 1), P(X_0 = 2)]$

$\mathbb{A} = \begin{bmatrix} P(X_1 = 1 \,\vert\, X_0 = 1) & P(X_1 = 2\,\vert\,X_0=1) \\ P(X_1 = 1\,\vert\,X_0=2) & P(X_1 = 2\,\vert\,X_0=2) \end{bmatrix}$

If we write out $\pi_1$ in terms of the matrix multiplication on the right-hand side of <span style="color: red;">(1)</span>, we get:

$P(X_1 = 1) = P(X_0 = 1)P(X_1 = 1\,\vert\,X_0=1) + P(X_0 = 2)P(X_1 = 1\,\vert\,X_0=2)$

$P(X_1 = 2) = P(X_0 = 1)P(X_1 = 2\,\vert\,X_0=1) + P(X_0 = 2)P(X_1 = 2\,\vert\,X_0=2)$

Hopefully this makes sense. The probability of being in state 1 at time 1 is equal to the probability that we start in state 1 at time 0 and stay in state 1, plus the probability that we start in state 2 and transition to state 1. ◼️

If we reach a point in time where $\pi = \pi \mathbb{A}$, we say that we have reached the stationary distribution of the Markov chain. Once we are in the stationary distribution, we can never leave. The stationary distribution is characterised by the global balance equations, which state

$\pi_i \sum_{j \neq i} A_{ij} = \sum_{j \neq i} \pi_j A_{ji}$, subject to $\sum_j \pi_j =1$.

Roughly speaking, this means that the net flow of probability into a state must equal the flow of probability out of the state in order for the distribution to stay constant.

#### Irreducibility

Some conditions are necessary in order for a unique stationary distribution to exist. We require that the Markov chain is irreducible and aperiodic. Irreducibility means that it is possible to get from any state to any other state; in other words, there are no absorbing states in which we can get stuck. 

Formally, irreducibility requires

$P(X_{t_{ij}} = j\,|\,X_0 = i) > 0$ for all $t_{ij} > 0$.   

Here, $t_{ij}$ is subscripted to account for the fact that the time step can be a different integer for any pair of states $i$ and $j$.

**Example (adapted from [1] p. 598):** The following Markov chain with states $X_t \in \{1, 2, 3, 4\}$ is clearly not irreducible.

<img src="figs/irreducible.pdf" alt="irreducible.pdf" style="zoom:250%;" /> 

We can never reach states 3 and 4 if we start from states 1 or 2. Similarly, we can never reach any other state if we start in state 4 (an absorbing state).

If we start in states 1 or 2, the stationary distribution is $\pi_{X_1 \in\{1, 2\}} = [0.5, \,0.5,\, 0,\, 0]$ (all transition probabilities are equal, so we expect to spend an equal amount of time in either state). Conversely, if we start in state 4 we never leave, so the stationary distribution is $\pi_{X_1 = 4} = [0,\, 0,\, 0,\, 1.0]$. If we start in state 3, we have a 50/50 chance of the stationary distribution being one of $\pi_{X_1 \in\{1, 2\}}$ or $\pi_{X_1 = 4}$. In other words, there is no unique stationary distribution. ◼️

#### Aperiodicity

The periodicity of a Markov chain describes the regularity with which we visit states. If a state is aperiodic, we return to this particular state irregularly. If all states in a Markov chain are aperiodic, then the Markov chain is aperiodic. Formally, the periodicity of state $i$ is defined as

$$d(i) = \textit{gcd}\{t > 0: P(X_t = i \,|\, X_0 = i) > 0\}$$,

where $d(i)$ denotes the periodicity of state $i$, $\textit{gcd}$ denotes the greatest common denominator and $P(X_t = i \,|\, X_0 = i)$ denotes the probability of returning to state $i$ after $t$ steps.

Intuitively, we require aperiodicity because if the chain were periodic, we would expect the probabilities of being in a certain state to vary with time.

#### Ergodicity

In the event that we are dealing with a Markov chain where the state-space is not finite, we require that the Markov chain is positive recurrent (recurrence is guaranteed for irreducible finite-state chains). This means that we require that the expected return-time to state $i$ is finite (given we start in state $i$). In other words, we will return to state $i$ with probability 1. 

A Markov chain that is irreducible, aperiodic and positive recurrent is called an ergodic Markov chain, and is guaranteed to have a limiting stationary distribution.

A sufficient but not necessary condition for ergodicity, and hence the existence of a unique stationary distribution, is that the Markov chain satisfies the detailed balance equations

$$\pi_i A_{ij} = \pi_j A_{ji}$$

for all pairs $i$ and $j$. If this holds, the global balance equations are satisfied (which can be seen by summing over $j$ on both sides) and $\pi$ is the stationary distribution.



## Monte Carlo

Monte Carlo (MC) approximation is a random sampling method that, among other things, allows us to estimate sums and integrals. MC is particularly helpful in problems where the desired sum or integral cannot be computed analytically.

To estimate the expected value of any function of a random variable $f(X)$ where $X \sim p(X)$ (read: $X$ is distributed according to $p(X)$), we generate $N$ samples $x_1, \ldots, x_N$ from $p(X)$ and approximate $f$ using the empirical distribution of $\{f(x_n)\}_{n=1}^N$:

$$\mathbb{E}[f(X)] = \int f(x)p(x) \,dx \approx \frac{1}{N} \sum_{n=1}^{N} f(x_n)$$.

It can be shown (under some restrictions) that the error of the MC approximation $(\hat{f} - f) \rightarrow \mathcal{N}\big(0, \frac{\sigma^2}{N}\big)$ as $N \rightarrow \infty$. This means that $\hat{f}$ is an unbiased estimator of $f$ and that it converges to the true $f$ as the number of samples $N$ gets large.

**Example:** A classic application of MC approximation is estimating $\pi = 3.1415926\ldots$ by calculating the area of a unit circle using random samples from a uniform distribution:

$$\pi \approx \frac{4}{N} \sum_{i=1}^N \mathbf{1}\big(x_i^2 + y_i^2 < 1\big), \quad x_i, y_i \sim U(0, 1).$$

Here $f(x, y) = 4 \cdot \mathbf{1}(x^2 + y^2 < 1)$.

(Try implementing it in Python!)



## Markov chain Monte Carlo

The main idea of Markov chain Monte Carlo (MCMC) methods is to construct a Markov chain over the parameter space where the stationary distribution is the posterior $p(\theta \,\vert\, y)$. We can then use the sequence of parameteres to calculate Monte Carlo approximations of any quantity of interest (hence the name Markov chain Monte Carlo).

A very general algorithmic view of MCMC is summarised in the following:

1. Start at your current position.

2. Propose a new position.

3. Decide whether or not to make the transition from your current position to the new position.

   a. If the proposal is rejected: remain in your current position, increment $t$ and return to step 1.

   b. If the proposal is accepted: move to the new position, increment $t$ and return to step 1.

4. After a large number of iterations, return the sequence of samples positions. These are your samples from the posterior distribution.

To reiterate: In the MCMC framework, we randomly move around the state space (parameter space) in such a way that the fraction of time we spend in each state (at each randomly sampled parameter value) is proportional to the true target density $p(\theta \,\vert\,y)$.

### Metropolis-Hastings

The Metropolis-Hastings (MH) algorithm is one of the most famous MCMC methods.

1. Start at some initial parameter value $\theta_0$.

2. For $t = 1, \ldots T$:
   a) Sample $\theta^*$ from a proposal distribution $q(\theta^* \, \vert \, \theta_{t-1})$.

   b) Draw $u \sim \mathcal{U}(0, 1)$.

   c) Evaluate $\alpha_{\theta^*}= \dfrac{p(\theta^* \, \vert \, y)}{p(\theta_{t-1} \, \vert \, y)} \cdot \dfrac{q(\theta_{t-1} \, \vert \, \theta^*)}{q(\theta^* \, \vert \, \theta_{t-1})}$.

   ​	Let the acceptance probability be given by $r_{\theta^*}= \text{min}(1, \alpha_{\theta^*})$.

   d) Set $\theta_t = \begin{cases}\theta^*, &\text{if}\ u < r \\ \theta_{t-1}, &\text{o.w.}\ \end{cases}$

The ratio of $q\text{'s}$ in $\alpha_{\theta^*}$ is called the Hastings correction, which corrects for asymmetric proposal distributions. Note that if the proposal distribution is symmetric $q(\theta^* \, \vert \, \theta_{t-1}) = q(\theta_{t-1} \, \vert \, \theta^*)$ then the acceptance probability becomes

$r_{\theta^*} = \text{min} \Bigg( 1, \dfrac{p(\theta^* \, \vert \, y)}{p(\theta_{t-1} \, \vert \, y)} \Bigg)$,

which is slightly easier to interpret. It says that we definitely accept proposals when we move to regions of higher density, i.e. when $p(\theta^* \, \vert \, y) > p(\theta_{t-1} \, \vert \, y)$. However, if  $p(\theta^* \, \vert \, y) < p(\theta_{t-1} \, \vert \, y)$, there is still some probability that we will move there regardless. This is important if we want to sample from the whole posterior.

**Why does this work?** If you are confused, that's normal. For instance, why do we use the target distribution in the expressions above when we have said that it is unknown? Consider the ratio 

$\dfrac{p(\theta^* \, \vert\,y)}{p(\theta \, \vert\, y)} = \dfrac{\dfrac{p(\theta^*) p(y\, \vert\,\theta^*)}{p(y)}}{\dfrac{p(\theta) p(y\, \vert\,\theta)}{p(y)}} = \dfrac{p(\theta^*) p(y\, \vert\,\theta^*)}{p(\theta) p(y\, \vert\,\theta)} = \dfrac{\tilde{p}(\theta^* \, \vert\,y)}{\tilde{p}(\theta \, \vert\, y)}$,

where $\tilde{p}(\theta \, \vert \, y) \propto p(\theta \, \vert \,y)$. This shows that we only need an expression that is proportional to the posterior density, because the problematic normalising constant cancels out. We already have this expression when formulating a Bayesian inference problem: It is the product of the prior and the likelihood, which are typically defined by us.

Secondly, how do we know that the sequence of parameters that result from the MH algorithm are in fact draws from the true posterior distribution $p(\theta \,\vert\, y)$? We can show this (adapted from [1] p. 856) by considering the transition probabilities of the Markov chain defined by the MH algorithm:

$P(X_t = \theta^* \,\vert\, X_{t-1} = \theta_{t-1}) = \begin{cases}q(\theta^* \, \vert \, \theta_{t-1})r_{\theta^*}, &\text{if}\ \theta^* \neq \theta_{t-1} \\ q(\theta_{t-1} | \theta_{t-1}) + \sum_{\theta^* \neq \theta_{t-1}} q(\theta^* \,\vert\, \theta_{t-1})[1 - r_{\theta^*}], & \text{o.w.} \end{cases}$ 

Let's decipher this. Consider the things that can happen in this chain:

1. We make the transition $\theta_{t-1} \rightarrow \theta^*$. This means we must have proposed $\theta^*$ and it was accepted with probability $r_{\theta^*}$.

2. We stay at $\theta_{t-1}$. This means one of two things:

   a. We proposed $\theta_{t-1}$ (which means that $r_{\theta_{t-1}} = 1$ and we accept), or

   b. We proposed $\theta^*$ and it was rejected with probability $1 - r_{\theta^*}$.

Recall that a Markov chain has a unique stationary distribution $\pi$ if it satisfies the detailed balance equations (here we adjust the notation to match the MH-setting):

$\pi_{\theta_{t-1}}P(X_t = \theta^* \,\vert\, X_{t-1} = \theta_{t-1}) = \pi_{\theta^*}P(X_t = \theta_{t-1} \,\vert\, X_{t-1} = \theta^*)$.

Now, consider the two states $\theta_{t-1}$ and $\theta^*$. Ignoring ties, either

1. $p(\theta^* \, \vert \, y)q(\theta_{t-1} \, \vert \, \theta^*) > p(\theta_{t-1} \, \vert \, y)q(\theta^* \, \vert \, \theta_{t-1})$, or

2. $p(\theta^* \, \vert \, y)q(\theta_{t-1} \, \vert \, \theta^*) < p(\theta_{t-1} \, \vert \, y)q(\theta^* \, \vert \, \theta_{t-1})$.

Without loss of generality, assume situation 2. This means

$\alpha_{\theta^*}= \dfrac{p(\theta^* \, \vert \, y)}{p(\theta_{t-1} \, \vert \, y)} \cdot \dfrac{q(\theta_{t-1} \, \vert \, \theta^*)}{q(\theta^* \, \vert \, \theta_{t-1})} < 1 \quad \Rightarrow \quad r_{\theta^*} = \alpha_{\theta^*}$.

To move from $\theta_{t-1} \rightarrow \theta^*$, we need to propose $\theta^*$ and accept it with probability $r_{\theta^*}$:

$\begin{align*}P(X_t = \theta^* \,\vert\, X_{t-1} = \theta_{t-1}) &= q(\theta^* \, \vert \, \theta_{t-1})r_{\theta^*} \\ &= q(\theta^* \, \vert \, \theta_{t-1})\dfrac{p(\theta^* \, \vert \, y)}{p(\theta_{t-1} \, \vert \, y)} \cdot \dfrac{q(\theta_{t-1} \, \vert \, \theta^*)}{q(\theta^* \, \vert \, \theta_{t-1})} \\ &= \dfrac{p(\theta^* \, \vert \, y)}{p(\theta_{t-1} \, \vert \, y)}q(\theta_{t-1} \, \vert \, \theta^*) \end{align*}$

which gives

(1) $p(\theta_{t-1} \, \vert \, y)P(X_t = \theta^* \,\vert\, X_{t-1} = \theta_{t-1}) = p(\theta^* \, \vert \, y)q(\theta_{t-1} \, \vert \, \theta^*)$.

The backwards probability is

(2) $P(X_t = \theta_{t-1} \,\vert\, X_{t-1} = \theta^*) = q(\theta_{t-1} \, \vert \, \theta^*)$,

since in this case $r_{\theta_{t-1}} = 1$ (as per our assumption).

Inserting (2) into (1) gives

$p(\theta_{t-1} \, \vert \, y)P(X_t = \theta^* \,\vert\, X_{t-1} = \theta_{t-1}) = p(\theta^* \, \vert \, y)P(X_t = \theta_{t-1} \,\vert\, X_{t-1} = \theta^*)$,

which satisfies detailed balance wrt. $p(\theta \,\vert\, y)$, and we have guaranteed that the stationary distribution of the Markov chain is the posterior target density of interest.



### Hamiltonian Monte Carlo (HMC)

Software like Stan and PyMC3 typically uses more complicated sampling algorithms due to the limitations of Metropolis-Hastings. One of the most efficient is the NUTS (No U-Turn Sampler) algorithm. Check the [Stan documentation](https://mc-stan.org/docs/2_21/reference-manual/hamiltonian-monte-carlo.html) for more details on HMC and NUTS.



## Resources

[1] Murphy, K. (2012). Machine Learning: A Probabilistic Perspective. 