# Ensemencer
An [esoteric programming language](https://esolangs.org/wiki/ensemencer).

Discover finite-state-automata by overlaying regions of the Mersenne twister!

Uses the standard Mersenne twister implementation MT19937 to seed its main memory space. Named after the French verb meaning 'to sow' (seeds).

Ensemencer has the following parts:

* an input buffer from which it can read user input, and also write data to.
* an instruction stream, which it reads byte by byte
* a data field, which is a series of 32 bit values seeded by a particular Mersenne twister seed (initialised to 0 before execution).

There is an instruction pointer, and a data pointer, which moves forwards one step (32bit Mersenne twister values) every read.

The Mersenne twister has a period of 2<sup>19937</sup>-1, when the instruction pointer reaches the end of the instruction stream, it reads the remaining bytes of the data field (to reset it), and also resets the instruction pointer to the beggining of the instruction stream.

The seed is generated using the MT19937 <code>init_genrand()</code> algorithm, which is limited to 32bit seeds. This is not the default in Python3 which uses the <code>init_by_array()</code> and can accept larger seeds. (I need to check the actual size limit for these seeds, I suspect up to 64bit system dependent seeds can be used, but these are scaled down to 32bit?)


## Commands:

| Command | Description |
| ------- | ----------- |
| `#`     | Read value from input buffer and set seed |
| `.`     | Output next data byte (`MT32bit >> 24`) |
| `{int [0-9]+}` | Read `{int}` data values and discard them |
| `?`     | Conditional skip, skip the next instruction byte if `MT32bit & 1` is true |
| `-`     | Next - skip remaining commands and begin program loop again |
| `<`     | Read data byte and insert at head of input stream |
| `!`     | Halt |
| `{EOF}` | Read the remainder of the data field (to 2<sup>19937</sup>-1) and reset instruction stream |

### Possible extensions:
* `>` read data byte and append to input stream
* `x` discard value from input buffer
* `@` read byte then read that many bytes and discard

## Input
Inupt values of any size can be passed to a program via any mechanism. In practice, for interactive input, the input will be limited to printable ASCII values generated by keyboard, or 8bit bytes read by the <code><</code> instruction.

## Data read
Data bytes are read by bit shifting the Mersenne twister 32bit data value right by 24 (getting the most significant 8bits). Truth tests using <code>?</code> are performed using the least significant bit of the 32bit value.


## Ideas for further exploration
**Don't** reset the seed / read the remaining data bytes when the instruction stream ends. This may allow multiple input states...

- [x] binary cat 0 -> 0, 1 -> 1
- [ ] multi-state FSM: duplicate first of a group of similar bits: e.g. 10011 -> 11000111

