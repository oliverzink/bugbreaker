import sys

import bugbreaker.utilities.chatgpt as gpt
import bugbreaker.utilities.parsers as parsers
import bugbreaker.utilities.printers as printers
import bugbreaker.utilities.code_execution as code_exec


def main():
    args = sys.argv
    if len(args) == 1 or args[1].lower() in ('-h', '--help'):
        printers.print_help_message()
        return
    language = parsers.get_language(args)
    if not language:
        printers.print_invalid_language_message()
        return
    if not gpt.is_user_registered():
        gpt.register_openai_credentials()

    error_message = code_exec.execute_code(args, language)
    if not error_message:
        return
    print()
    with printers.LoadingMessage():
        explanation = gpt.get_chatgpt_explanation(language, error_message)

    printers.print_error_explanation(explanation)
