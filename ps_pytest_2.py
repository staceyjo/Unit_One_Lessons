# ================================================ test session starts ================================================
# platform darwin -- Python 3.8.5, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
# rootdir: /Users/user/projects/project
# collected 1 item

# main.py F                                                                                                     [100%]

# ===================================================== FAILURES ======================================================
# _______________________________________________ test_mystery_function _______________________________________________

#     def test_mystery_function():
# >       assert mystery_function("apples", "oranges") == False
# E       TypeError: mystery_function() takes 0 positional arguments but 2 were given

# main.py:31: TypeError
# ============================================== short test summary info ==============================================
# FAILED main.py::test_mystery_function - TypeError: mystery_function() takes 0 positional arguments but 2 were given
# ================================================= 1 failed in 0.08s =================================================



# We reach this conclusion using the following lines:

# >       assert mystery_function("apples", "oranges") == False
# E       TypeError: mystery_function() takes 0 positional arguments but 2 were given

# main.py:31: TypeError
# ============================================== short test summary info ==============================================
# FAILED main.py::test_mystery_function - TypeError: mystery_function() takes 0 positional arguments but 2 were given
# The line marked > shows the line where the error was encountered.
# The line marked E shows what error was encountered.
# main.py:31: TypeError reinforces that a TypeError occurred during the test.
# In the summary, the FAILED notice repeats any error messages from this test and any others which may have been found.
# The line marked > shows the line where the error was encountered.
# The line marked E shows what error was encountered.
# main.py:31: TypeError reinforces that a TypeError occurred during the test.
# In the summary, the FAILED notice repeats any error messages from this test and any others which may have been found.