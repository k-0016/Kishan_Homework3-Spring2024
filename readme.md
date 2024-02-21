Achievements for Grading
30 Points - Faker Integration
Achievement: Successfully integrated the Faker library to generate dynamic and realistic test data for the calculator application.
Evidence: Implemented in conftest.py, Faker generates diverse operands and operations, enhancing the robustness of tests by covering a wide range of input scenarios, including edge cases.
30 Points - Test Data Generation
Achievement: Utilized dynamic test data generation, leveraging pytest's capabilities and the Faker library to create flexible and comprehensive test scenarios.
Evidence: Demonstrated through the use of pytest_generate_tests in conftest.py and the fixture setup to dynamically parameterize tests based on Faker-generated data, ensuring extensive test coverage across various input types and operations.
40 Points - User Input
Achievement: Implemented comprehensive user input handling, supporting both symbolic and textual representations of operations, robust error handling for invalid inputs, and managing inputs with varying amounts of whitespace.
Evidence: Showcased in main.py with the implementation of parse_user_input and calculate_and_print functions. These functions collectively handle parsing user inputs (including both symbols and text for operations), executing calculations, and providing clear error messages for unsupported operations or input errors.