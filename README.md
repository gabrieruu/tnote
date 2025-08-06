# tnote

## Description

**tnote** is a lightweight command-line app to store and quickly retrieve your personal tech references — keybindings, commands, methods, shortcuts, or any snippet of knowledge you often need but hate digging through documentation to find.

Whether it's a `vim` shortcut, a handy `docker` command, or a Python object method you keep forgetting, **tnote** helps you save and access it in seconds — right from your terminal.
https://www.python.org/downloads/

## Features

- Save and retrieve short technical notes using simple titles
- Organize by tools
- Lightning-fast lookup from the CLI
- Local, plain-text storage 
- Future support for opening official docs in your browser

## Requirements

This project requires the following tools:

- [python](https://www.python.org/downloads/)
- [pip](https://github.com/pypa/pip)

## Installation

Clone the repository and navigate to the root directory:

```bash
git clone https://github.com/gabrieruu/tnote
cd tnote
```

Install as a python package:

```bash
pip install .
```

Run tnote:

```bash
tnote -h
```

## Usage

Run tnote:

```bash
tnote
```

### Add a Tool

```bash
tnote add tool -n "tool name"
```

### Add a Reference

```bash
tnote add reference -t "tool name" -n "reference name" -c "content"
```

### List/Read References

```bash
tnote list
```

### Remove Tools/References

```bash
tnote remove {tool, reference}
```
* Removing a tool deletes all related references.

## Contributing

If you'd like to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'feat: add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

Please follow the commit standards outlined below.

### Commit Standards

This project follows the [Conventional Commits](https://www.conventionalcommits.org/) specification:

Examples:

* `feat: add new user login feature`
* `fix: resolve crash on missing input`
* `docs: update contributing guidelines`
* `style: reformat code with black`
* `refactor: simplify command parsing`
* `test: add unit tests for AddCommand`
* `chore: update dependencies`

Use the format `<type>: <description>` in your commit messages. For larger changes, consider adding a scope like `<type>(parser): <description>`.

### Local Development
WIP
