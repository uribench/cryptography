# Book Ciphers

In cryptography, a book cipher is an encryption technique that uses letters of subsequent words in a
given text or book as a key to encrypt messages.

The code examples here are using a variant of the book cipher algorithm. Letters of subsequent 
words in some text are picked based on some index computation over a given sequence of numbers
(running keys). The picked letters are the secrete message.

## Code Examples

The following examples for book cipher are provided:

- book_cipher_async
- book_cipher_sync

Both are sharing the same ciphering engine. One is employing an asynchronous programing model, while
the other is a simpler one using the synchronous programing model.

### Book Cipher Async

This book cipher employs an asynchronous programing model using a common pattern with a Promise
function and a generator function.

The generator function (specified by the `function` keyword followed by an asterisk) returns a 
Generator object that is consumed by the the inner loop of the Promise function.

### Book Cipher Sync

This book cipher is using the simpler synchronous programing model with exactly the same ciphering 
engine as in the asynchronous example.

## Cipher Code Description

Let's focus on the description of the cipher principle, and ignore the boilerplate of the 
asynchronous model pattern.

In the attached code for instance, the following words and keys are used:

```javascript
const secret = {
  words: [
    'Redundant', 'comments', 'merely', 'collect', 'deceptive', 'descriptions'],
  keys: [
    4, 2, 3, 4, 5, 2, 3, 5, 2, 2,
    1, 0, 2, 7, 3, 4, 2, 4, 7, 6,
    0, 1, 6, 2, 4, 6, 4, 1, 6, 4,
    1, 0, 6, 2, 7, 3, 7, 6, 1, 0,
    0, 0, 1, 4, 3, 3, 5, 0, 1, 6,
    0, 5, 4, 6, 7, 0, 6, 2, 1, 4]
};
```

Since there are 6 words in this example, we expect the calculations over the keys to generate 6
indices, one for each word. These indices will pick one letter from each word.

The heart of the ciphering engine is:

```javascript
words.shift()[keys.splice(0, 10).reduce((a, b) => a ^ b, 0)];
```

In both examples it is executed inside a loop `while (words.length) {...}`.

The loop will have 6 iterations, which is equal to the number of items in the `words` array. 

The `shift()` method removes the first element from an array and returns that element. This method 
changes the length of the array.

Therefore, the operation `words.shift()` inside the above loop, will return all the 6 items in 
`words` one by one from left (first element) to the right (last element).

The `splice()` method changes the contents of an array by removing existing elements and/or adding 
new elements.

The operation `keys.splice(0, 10)` returns the first 10 items of the `keys` array. When called 
within the loop `while (words.length) {...}` it will return the next 10 items of the `keys` array,
in each of the 6 iterations.

The `reduce()` method executes a provided reducer function on each member of the array, resulting in 
a single output value.

The operation `reduce((a, b) => a ^ b, 0)` has the syntax of `arr.reduce(callback, initialValue)`.

The `callback` function here is an anonymous function (lambda expression) `(a, b) => a ^ b`.

The provided `initialValue` in this case is equal to `0`.

The first parameter of the reducer callback function (i.e., `a` ) is the accumulator. The 
accumulator accumulates the callback's return values; it is the accumulated value previously 
returned in the last invocation of the callback, or initialValue, if supplied.

The second parameter of the reducer callback function (i.e., `b` ) is the currentValue. The current 
element being processed in the array.

The optional third parameter for a reducer callback function, called currentIndex, is not used here. 
The index of the current element being processed in the array. Starts at index 0, if an initialValue 
is provided, and at index 1 otherwise.

The operation `keys.splice(0, 10).reduce((a, b) => a ^ b, 0)` will perform XOR (exclusive or) 
calculation on each batch of 10 digits of keys. When called 6 times, each with the next 10 items of 
`keys`, it will return the following results : 0, 4, 0, 1, 7, 1

When combined with the following operation in the above loop
`words.shift()[keys.splice(0, 10).reduce((a, b) => a ^ b, 0)]`
the results of the `reduce` will index each of the items in `words` in its turn (from left-to-right)
as follows:

- Iteration 1: String `'Redundant'` will be indexed by [0] returning `'R'`
- Iteration 2: String `'comments'` will be indexed by [4] returning `'e'`
- ...
- Iteration 6: String `'descriptions'` will be indexed by [1] returning `'e'`

All the iterations will return the string 'Remove'.

## Long XOR Calculation Example

As an example, let's examine in details how the reduce returns `0` for the first 10 items of `keys`: 
`[4, 2, 3, 4, 5, 2, 3, 5, 2, 2,]`.

One call of the reduce will work on the 10 digits of `keys` as follows:

Reminder: `a` is accumulator and `b` is the current value. The result for each calculation will be 
stored in `a` for the next calculation.

1. a = 0, b = 4, a ^ b = 4
2. a = 4, b = 2, a ^ b = 6
3. a = 6, b = 3, a ^ b = 5
4. a = 5, b = 4, a ^ b = 1
5. a = 1, b = 5, a ^ b = 4
6. a = 4, b = 2, a ^ b = 6
7. a = 6, b = 3, a ^ b = 5
8. a = 5, b = 5, a ^ b = 0
9. a = 0, b = 2, a ^ b = 2
10. a = 2, b = 2, a ^ b = 0

Final result for this call to reduce function is 0, as expected.

## Quick XOR Calculation on a Large Sequence of Digits

A manual XOR calculation on a large sequence of digits does not need to be exhaustive. In stead of
calculating XOR on all the digits, the following simplified approach can be used:

- Step_1: eliminate all digits that are having even number of repetitions,
- Step_2: make from the remaining digits a list (without duplicate values), 
- Step_3: check the resulting list and continue as follows:

    - Rule_1: If the result list has at least 2 members, then calculate the XOR for them.
    - Rule_2: else-if the result is an empty list (meaning, all the digits in the given list are 
              having even number of repetitions), then the result is zero.
    - Rule_3: else-if the result list has exactly 1 member, then this member is the result. Note, 
              this rule will never be triggered with a given list that is having an even number of 
              digits (e.g., 10 in our case).

Examples:

1. The second batch of the keys is a good example for Rule_1:
    - Given: 1, 0, 2, 7, 3, 4, 2, 4, 7, 6,
    - After removing digits with even number of duplications, we are left with: 1, 0, 3, 6
    - Calculating the XOR on 1, 0, 3, 6 gives 4, as expected.

2. The first batch of the keys is a good example for Rule_2:
    - Given: 4, 2, 3, 4, 5, 2, 3, 5, 2, 2,
    - After removing digits with even number duplications we are left with: empty list
    - No need to calculate XOR, as we were left with an empty list and the result according to the 
      second rule is 0, as expected

Note that the above rules are relying on the fact that Bitwise XOR operator is both Commutative and 
Associative.

## Composing a Sequence of Digits for a given XOR Result

It is interesting to see how the digits of the above `keys` array were selected.

The first 9 digits of a keys batch (i.e., 10 items) can be selected randomly. The 10th item has to 
be selected in such a way that its XOR with the XOR of all the first 9 digits (i.e, the result of 
the above reduce function for the first 9 items) will yield the desired final reduce value.
