# Code examples 

## [Hello, World!](hw.ens)
Uses the default seed of 0 to produce the traditional `Hello, World!` output.

## [Binary cat](bincat.ens)
Binary `cat` program. Echos character input from the set `{"0", "1"}`. It has a side effect of converting newlines into `·`. Other characters will be arbitrarily converted.

## [Inverse binary cat](invbincat.ens)
Similar to the above but outputs `0` for `1`, `1` for `0`.

## [Integer Truth machine](truth.ens)
A Truth machine is a simple program form that demonstrates input, decision making, and looping behaviour.
Integer input: `{0, 1}`.

## [Character Truth machine](truth_char.ens)
Character input: `{"0", "1"}`.


## [Parity machine](parity.ens)
Implements a multistate FSM from an example in Minksy's [_Computation: Finite and Infinite Machines_, **Fig 2.3-2** (p.21)](https://archive.org/details/computationfinit0000mins/page/21)

The last `0`/`1` output indicates whether an odd number of 1's have been received as input over the history of the machine's operation.

This code has a side effect where a line-feed input (ASCII 10) produces output rc in one of the states. This was unintentional, but further demonstrates that the machine can be in two distinct states. The alphabetic characters to the right are NOPs and demonstrate a method of commenting. The purpose of this example is to prove that by locating sufficient skips based on varying seeds, multiple distinct states can be implemented in this language.
