# Ensemencer

Uses the Mersenne twister to seed its main memory space. Named after the French verb meaning 'to sow' (seeds).

Ensemencer has the following parts:

* an input buffer from which it can read user input, and also write data to (append or prepend).
* an instruction stream, which it reads byte by byte
* a data field, which is a series of bytes seeded by a particular Mersenne twister seed (which is initialised to 0 before execution)

There is an instruction pointer, and a data pointer, which moves forwards one step every read.

The Mersenne twister has a period of 2<sup>19937</sup>-1, when the instruction pointer reaches the end of the instruction stream, it reads the remaining bytes of the data field (to reset it), and also resets the instruction stream.


## Instructions:

* `#` read value from input buffer and set seed
* `.` output next data byte 
* `<int [0-9]+>` read `<int>` data bytes and discard them
* `?` conditional, only execute next instruction if data byte & 1 is true
* `!` halt

* `<` read data byte and insert at head of input stream
* `{EOF}` read the remainder of the data field (to 2<sup>19937</sup>-1) and reset instruction stream

### Possible instructions:
* `-` next - skip remaining commands and begin progam loop again
* `>` read data byte and append to input stream
* `x` discard value from input buffer
* `@` read byte then read that many bytes and discard


## Ideas
**Don't** reset the seed / read the remaining data bytes when the instruction stream ends. This may allow multiple input states...

- [x] binary cat 0 -> 0, 1 -> 1
- [ ] multi-state FSM: duplicate first of a group of similar bits: e.g. 10011 -> 11000111
