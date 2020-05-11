from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField, FileField
from wtforms.validators import DataRequired, ValidationError

from werkzeug.utils import secure_filename


class FormAddGroup(FlaskForm):
    name = StringField('Название', validators=[DataRequired(message="Поле должно быть заполнено")])
    leader_id = IntegerField("id руководителя", validators=[DataRequired(message="Поле должно быть заполнено")])
    info = TextAreaField("Информация о факультативе")
    photo = FileField("Загрузить фотографию на факультатив")
    submit = SubmitField('Отправить')

    def validate_photo(self, field):
        if field.data:
            filename = secure_filename(field.data.filename)
            if filename.rsplit('.', 1)[1] not in ('png', 'jpeg', 'jpg'):
                raise ValidationError("Недопустимое расширение для фото, используйте .png или .jpeg(.jpg)")
