import re
import logging

# Configure logging to show messages on the console
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class LaunchAuthorizationSystem:
    """
    Validates nuclear launch authorization codes using a predefined pattern.
    """

    # Expected format: AUTH-XXXXXX-YYYY-SECURE (where X = uppercase letter/number, Y = digit)
    _AUTH_CODE_REGEX = r"^AUTH-[A-Z0-9]{6}-\d{4}-SECURE$"

    @staticmethod
    def validate_code(auth_code):
        """
        Checks if the provided authorization code matches the required secure pattern.

        Parameters:
            auth_code (str): The authorization code to be validated.

        Returns:
            bool: True if the code is valid, False otherwise.
        """
        if re.fullmatch(LaunchAuthorizationSystem._AUTH_CODE_REGEX, auth_code):
            logging.info("Authorization code is valid.")
            return True
        else:
            logging.warning("Authorization code is invalid.")
            return False
