Rules
Coding Conventions
1.	Naming Conventions
  o	Variables and Functions: Use snake_case (e.g., process_suite_metadata, get_from_tags).
  o	Classes: Use PascalCase (e.g., Logger, CRQMClient).
  o	Constants: Use all uppercase letters with underscores (e.g., DEFAULT_METADATA, DRESULT_MAPPING).
2.	Indentation
  o	Consistent use of 4 spaces per indentation level.
  o	No tabs are used.
3.	Imports
  o	Standard library imports are listed first, followed by third-party and then local imports.
  o	Imports are grouped and separated by blank lines.
4.	Whitespace
  o	Spaces after commas and around operators.
  o	No trailing whitespace at the end of lines.
  o	Blank lines separate logical sections of code.
5.	Error Handling
  o	Use of try...except blocks for exception handling.
  o	Custom error and warning logging via the Logger class.
6.	File Structure
  o	Copyright and license information at the top.
  o	Main execution guarded by if __name__ == "__main__":.

Docstring Conventions
1.	Format
  o	Triple double quotes (""") for docstrings.
  o	Docstrings are provided for modules, classes, and functions.
2.	Content
  o	Each docstring starts with a short summary of the function/class/module.
  o	Arguments are listed with their names, conditions, types, and defaults.
  o	Return values are described with types and explanations.
  o	Some docstrings include usage examples or code snippets.
3.	Style
  o	Parameters and return values are documented in a structured, readable format.
  o	Use of bullet points and indentation for clarity.
  o	Consistent phrasing: "Arguments:", "Returns:", "Example:", etc.

Refs:
* PEP 8 – Style Guide for Python Code
* PEP 257 – Docstring Conventions
