import random
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from model_utils.models import TimeStampedModel
from account.models import CustomUserModel


class Question(TimeStampedModel):
    ALLOWED_NUMBER_OF_CORRECT_CHOICES = 1

    html = models.TextField(_('Soru'))
    is_published = models.BooleanField(_('Yayınlandı mı?'), default=False, null=False)
    maximum_marks = models.DecimalField(_('Maksimum Puanlar'), default=4, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.html

    class Meta:
        db_table = 'Soru'
        verbose_name = 'Soru'
        verbose_name_plural = 'Sorular'


class Choice(TimeStampedModel):
    MAX_CHOICES_COUNT = 4

    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    is_correct = models.BooleanField(_('Bu cevap doğru mu?'), default=False, null=False)
    html = models.TextField(_('Secenekler'))

    def __str__(self):
        return self.html

    class Meta:
        db_table = 'Seçenek'
        verbose_name = 'Seçenek'
        verbose_name_plural = 'Seçenekler'


class QuizProfile(TimeStampedModel):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
    total_score = models.DecimalField(_('Toplam puan'), default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return f'<QuizProfile: user={self.user}>'

    def get_new_question(self):
        used_questions_pk = AttemptedQuestion.objects.filter(quiz_profile=self).values_list('question__pk', flat=True)
        remaining_questions = Question.objects.exclude(pk__in=used_questions_pk)
        if not remaining_questions.exists():
            return
        return random.choice(remaining_questions)

    def create_attempt(self, question):
        attempted_question = AttemptedQuestion(question=question, quiz_profile=self)
        attempted_question.save()

    def evaluate_attempt(self, attempted_question, selected_choice):
        if attempted_question.question_id != selected_choice.question_id:
            return

        attempted_question.selected_choice = selected_choice
        if selected_choice.is_correct is True:
            attempted_question.is_correct = True
            attempted_question.marks_obtained = attempted_question.question.maximum_marks

        attempted_question.save()
        self.update_score()

    def update_score(self):
        marks_sum = self.attempts.filter(is_correct=True).aggregate(
            models.Sum('marks_obtained'))['marks_obtained__sum']
        self.total_score = marks_sum or 0
        self.save()


class AttemptedQuestion(TimeStampedModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    quiz_profile = models.ForeignKey(QuizProfile, on_delete=models.CASCADE, related_name='attempts')
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True)
    is_correct = models.BooleanField(_('Bu girişim doğru muydu?'), default=False, null=False)
    marks_obtained = models.DecimalField(_('Elde Edilen İşaretler'), default=0, decimal_places=2, max_digits=6)

    def get_absolute_url(self):
        return f'/submission-result/{self.pk}/'
