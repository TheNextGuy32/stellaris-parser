@{%
const moo = require("moo");

// I'm not bothering to make each of these tokenizers full proof as I'm assuming the input
// will be an actual list of problems.
const lexer = moo.compile({
  comment: /\#.*?/,
  string: /"("
  newline: {match: /\n/, lineBreaks: true}
});
%}

@lexer lexer

@builtin "number.ne"