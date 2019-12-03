# An introduction to Markov Chain Monte Carlo

WRITE BRIEF INTRODUCTION.



## Markov chains

A Markov chain is a way of defining a joint probability distribution over sequences. Markov chains are used to model many interesting things, such as industrial manufacturing processes, social mobility, queuing systems, etc. Famously, Markov chains were instrumental in the development of the PageRank algorithm of Google fame.

Another interpretation of Markov chains is that they are dynamical stochastic systems, where we jump from one state to another at each time step. Typically we are interested in the long-term distribution of being in a certain state. Markov chains can be used to model events in discrete and continuous time. 

In this section we will briefly cover the product rule of probability before giving a basic introduction to Markov chains. We spend some time discussing the stationary distribution, as it is central to the main idea of Markov Chain Monte Carlo methods.

### The product rule

Any joint probability distribution can be written as the product of conditional distributions. Consider the following example of the joint probability distribution over the random variables $X_1, X_2, X_3$ and $X_4$:

$$P(X_1, X_2, X_3, X_4) = P(X_1)P(X_2\,|\,X_1)P(X_3\,|\,X_2, X_1)P(X_4\,|\,X_3, X_2, X_1)$$.

This is also known as the product rule of probability, which we will revisit shortly.

### Markov chain basics

A Markov chain typically models a sequence of observations $X_1, X_2,\ldots, X_T$ for some arbitrary $T$. The subscript $t \in T$ can for example denote a time step, but it can also denote the location within a sequence. From now on we simply refer to $t$ as the time step, and we assume that $t$ is discrete, i.e. $t \in \{1, \,\ldots, T\}$. 

The fundamental assumption of a Markov chain is that the present time step contains all the information we need when making predictions about the next time step:

$$P(X_t\,|\,X_{t-1}, X_{t-2}, \ldots, X_1) = P(X_t\,|\,X_{t-1})$$.

This is sometimes referred to as the memoryless property. The joint distribution of a sequence of $T$ event can thus be factorised according to the product rule, but this time incorporating the Markov property:

$$P(X_1, X_2, \,\ldots, X_T) = P(X_1)P(X_2\,|\,X_1)P(X_3\,|\,X_2)\,\ldots = P(X_1) \prod_{i=2}^{T}P(X_t\,|\,X_{t-1})$$

When the state-space of $X_t$ is discrete, so $X_t \in \{1, \,\ldots, K\}$, we have what is called a finite-state Markov chain. We will limit ourselves to these types of models for simplicity.

### Visualising Markov chains

Markov chains can be represented graphically, like in the following figure:

 <img src="figs/simple_example.pdf" alt="simple_example.pdf" style="zoom:250%;" />

Each node is a state, and the directed edges connecting the nodes denote the probability of transitioning from one state to the next.

These transition probabilities can be described by a $K \times K$ matrix $\mathbb{A}$ with rows indexed bu $i$ and columns indexed by $j$. $\mathbb{A}$ Is called a transition matrix or a stochastic matrix, and $A_{ij} = P(X_t=j\,|\,X_{t-1} = i)$ is the probability of transitioning from state $i$ to state $j$ at time $t$. If $\mathbb{A}$ is constant over time, we call the Markov chain homogenous or time-invariant (from here on we assume that our Markov chains are time-homogenenous).

As an example, the transition matrix for the figure above would be

$\mathbb{A} = \begin{bmatrix} 0.1 & 0.9 \\ 0.8 & 0.2 \end{bmatrix}$.

Note that the row probabilites are constrained to sum to 1, i.e. $\sum_{j} A_{ij} = 1$. 

### The stationary distribution

Often we are interested in the long-term distribution over states. For example, what is the long run probability of being in state 2 in the example above?

Generally, given some initial distribution $\pi_0 = [P(X_0 = 1), \ldots, P(X_0 = K)]$ describing the probability of starting in a particular state at time $t=0$, the probability distribution over states at time $t=1$ is given by

$$\pi_1 = \pi_0 \mathbb{A}$$.

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

If we start in states 1 or 2, the stationary distribution is $\pi_{X_1 \in\{1, 2\}} = [0.5, \,0.5,\, 0,\, 0]$ (all transition probabilities are equal, so we expect to visit each state an equal amount). Conversely, if we start in state 4, the stationary distribution is $\pi_{X_1 = 4} = [0,\, 0,\, 0,\, 1.0]$. If we start in state 3, we have a 50/50 chance of the stationary distribution being one of $\pi_{X_1 \in\{1, 2\}}$ or $\pi_{X_1 = 4}$. In other words, there is no unique stationary distribution.

#### Aperiodicity

The periodicity of a Markov chain describes the regularity with which we visit states. If a state is aperiodic, this means we return to this particular state irregularly. If all states in a Markov chain are aperiodic, then the Markov chain is aperiodic. Formally, the periodicity of state $i$ is defined as

$$d(i) = \textit{gcd}\{t > 0: P(X_t = i \,|\, X_0 = i) > 0\}$$,

where $d(i)$ denotes the periodicity of state $i$, $\textit{gcd}$ denotes the greatest common denominator and $P(X_t = i \,|\, X_0 = i)$ denotes the probability of returning to state $i$ after $t$ steps.

Intuitively, we require aperiodicity because if the chain were periodic, we would expect the probabilities of being in a certain state to vary with time.

#### Ergodicity

In the event that we are dealing with a Markov chain where the state-space is not finite, we require that the Markov chain is positive recurrent (recurrence is guaranteed for irreducible finite-state chains). This means that we require that, given we start in state $i$, the expected return-time to state $i$ is finite. In other words, we will return to state $i$ with probability 1. A Markov chain that is irreducible, aperiodic and positive recurrent is called an ergodic Markov chain, and guaranteed to have a limiting stationary distribution.

A sufficient but not necessary condition for ergodicity, and hence the existence of a unique stationary distribution, is that the Markov chain satisfies the detailed balance equations

$$\pi_i A_{ij} = \pi_j A_{ji}$$

for all pairs $i$ and $j$. If this holds, the global balance equations are satisfied (which can be seen by summing over $j$ on both sides) and $\pi$ is the stationary distribution.



## Monte Carlo methods

TODO.



## Interlude

Bayes.



## Markov Chain Monte Carlo

TODO.

Introduce $p(\theta \,|\, y)$.



## Resources

[1] Murphy, K. (2012). Machine Learning: A Probabilistic Perspective. 