# Legacy Order Service (Internal Tooling Example)

This repository simulates a simplified order processing service used by internal engineering teams.

## Known Pain Points

- No validation on inputs
- No unit tests
- Business logic mixed with data handling
- No error handling for malformed orders
- Difficult to extend for new pricing rules
- No observability or logging

## Engineering Backlog

Teams have reported needing:

- Better test coverage
- Refactored pricing logic
- Input validation layer
- Separation of concerns between modules
- Support for discount rules (not yet implemented)

## This is where Devin is evaluated

We are exploring whether an AI engineering agent can:
- Improve code quality
- Add missing tests
- Refactor safely without breaking functionality
- Extend system functionality based on requirements
