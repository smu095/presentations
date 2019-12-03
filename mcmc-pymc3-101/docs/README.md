# An introduction to Markov Chain Monte Carlo

WRITE BRIEF INTRODUCTION.



## Markov chains

A Markov chain is a way of defining a joint probability distribution over sequences. Markov chains are used to model many interesting things, such as industrial manufacturing processes, social mobility, queuing systems, etc. Famously, Markov chains were instrumental in the development of the PageRank algorithm of Google fame.

Another interpretation of Markov chains is that they are dynamical stochastic systems, where we jump from one state to another at each time step. Typically we are interested in the long-term distribution of being in a certain state. Markov chains can be used to model events in discrete and continuous time. 

### The product rule

For instance, any joint probability distribution can be written as the product of conditional distributions. Consider the following example of the joint probability distribution over the random variables $X_1, X_2, X_3$ and $X_4$:

$$P(X_1, X_2, X_3, X_4) = P(X_1)P(X_2\,|\,X_1)P(X_3\,|\,X_2, X_1)P(X_4\,|\,X_3, X_2, X_1)$$.

This is also known as the product rule of probability.

A Markov chain typically models a sequence of observations $X_1, X_2,\ldots, X_T$ for some arbitrary $T$. The subscript $t \in T$ can for example denote a time step, but it can also denote the location within a sequence. From now on we simply refer to $t$ as the time step, and we assume that $t$ is discrete, i.e. $t \in \{1, \,\ldots, T\}$. 

### Markov chain basics

The fundamental assumption of a Markov chain is that the present time step contains all the information we need when making predictions about the next time step. This is sometimes referred to as the memoryless property. This can be expressed mathematically as

$$P(X_1, X_2, \,\ldots, X_T) = P(X_1)P(X_2\,|\,X_1)P(X_3\,|\,X_2)\,\ldots = P(X_1) \prod_{i=2}^{T}P(X_t\,|\,X_{t-1})$$

When the observations $X_t$ are discrete, so $X_t \in \{1, \,\ldots, K\}$, we have what is called a finite-state Markov chain. In the following we limit ourselves to these types of models for simplicity.

Markov chains can be represented graphically. Each node is a state, and the directed edges connecting the nodes denote the probability of transitioning from one state to the next.

TODO: Simple example figure here.

The transition probabilities between states can be described by a $K \times K$ matrix $\mathbb{A}$, known as a transition matrix or a stochastic matrix, where $A_{ij} = P(X_t=j\,|\,X_{t-1} = i)$ is the probability of transitioning from state $i$ to state $j$ at time $t$. Note that the row probabilites are constrained to sum to 1, i.e. $\sum_{j} A_{ij} = 1$. If $\mathbb{A}$ is constant over time, we call the Markov chain homogenous or time-invariant. From here on we assume that our Markov chains are time-homogenenous.

For example, the transition matrix for figure 1 would be...

### The stationary distribution

Often we are interested in the long-term distribution over states. 

GIVE BRIEF EXAMPLE. 

Given some initial distribution $\pi_0$ (typically assumed to be a row vector) describing the probability of starting in a particular state at time $t=0$, the probability distribution over states at time $t=1$ is given by

$$\pi_1 = \pi_0 \mathbb{A}$$.

If, after a while, we reach a point where $\pi = \pi \mathbb{A}$, we say that we have reached the stationary distribution. Once we are in the stationary distribution, we can never leave. The stationary distribution is characterised by the global balance equations, which state

$\pi_i \sum_{j \neq i} A_{ij} = \sum_{j \neq i} \pi_j A_{ji}$, subject to $\sum_j \pi_j =1$.

INTUITION.

Some conditions are necessary in order for a unique stationary distribution to exist is that the Markov chain is irreducible, aperiodic and that it has no absorbing states. Irreducibility means that it is possible to get from any state to any other state. Expressed mathematically, irreducibility requires

$P(X_{t_{ij}} = j\,|\,X_0 = i) > 0$ for all $t_{ij} > 0$.   

Here, $t_{ij}$ is subscripted to account for the fact that it can be a different integer for any pary of states $i$ and $j$.

The periodicity of a Markov chain describes the regularity with which we visit states. If a state is aperiodic, this means we return to this particular state irregularly. If all states in a Markov chain are aperiodic, then the Markov chain is aperiodic. Formally, the periodicity of state $i$ is defined as

$$d(i) = \textit{gcd}\{t > 0: P(X_t = i \,|\, X_0 = i) > 0\}$$,

where $d(i)$ denotes the periodicity of state $i$, $\textit{gcd}$ denotes the greatest common denominator and $P(X_t = i \,|\, X_0 = i)$ denotes the probability of returning to state $i$ after $t$ steps.

INTUITION.

Finally, for a unique limiting stationary distribution to exist for finite-state Markov chains, we require that there are no absorbing states.

FOR EXAMPLE.

In the event that we are dealing with a Markov chain where the state-space is not finite, we require that the Markov chain is positive recurrent. This means that we require that the expected return-time to this state is finite. A Markov chain that is irreducible, aperiodic and positive recurrent is guaranteed to have a limiting stationary distribution.

DETAILED BALANCE.



## Monte Carlo methods

TODO.



## Markov Chain Monte Carlo

TODO.