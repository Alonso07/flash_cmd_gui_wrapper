

class Controller:
    def __init__(self, model, views):
        self.model = model
        self.views = views

    def save(self, email):
        """
        Save the email
        :param email:
        :return:
        """
        try:

            # save the model
            self.model.email = email
            self.model.save()

            # show a success message
            self.views.show_success(f'The email {email} saved!')

        except ValueError as error:
            # show an error message
            self.views.show_error(error)   