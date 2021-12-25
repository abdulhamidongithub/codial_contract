from django.db import models

class Student(models.Model):
    JINS = (
        ("o'g'il", "o'g'il"),
        ("qiz", "qiz"),
    )
    ism = models.CharField(max_length=20)
    familiya = models.CharField(max_length=20)
    sharif = models.CharField(max_length=20, blank=True, null=True)
    jins = models.CharField(max_length=12, choices=JINS)
    tel1 = models.CharField(max_length=13)
    tel2 = models.CharField(max_length=13, blank=True)
    def __str__(self):
        return f"{self.ism} {self.familiya}"

class Kurs(models.Model):
    nom = models.CharField(max_length=20)
    narx = models.IntegerField()

    def __str__(self):
        return f"{self.nom}"


class Ustoz(models.Model):
    ism = models.CharField(max_length=25)
    familiya = models.CharField(max_length=25)

    def __str__(self):
        return self.ism

class Shartnoma(models.Model):
    KUN = (
        ("Dushanba-Juma", "Dushanba-Juma"),
        ("Seshanba-Shanba", "Seshanba-Shanba")
    )
    VAQT = (
        ("08:00-10:00", "08:00-10:00"),
        ("10:00-12:00", "10:00-12:00"),
        ("14:00-16:00", "14:00-16:00"),
        ("16:00-18:00", "16:00-18:00"),
        ("18:00-20:00", "18:00-20:00"),
    )
    S = (
        ("Active", "Active"),
        ("Passive", "Passive")
    )
    shartnoma_raqami = models.SmallIntegerField()
    sinov_dars_sanasi = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    ustoz = models.ForeignKey(Ustoz, on_delete=models.CASCADE)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    kunlar = models.CharField(max_length=30, choices=KUN)
    vaqt = models.CharField(max_length=20, choices=VAQT)
    guruh_nomi = models.CharField(max_length=15)
    student_holati = models.CharField(max_length=15, choices=(("yangi", "yangi"), ("loyal", "loyal")))
    status = models.CharField(max_length=10, choices=S)
    tuzuvchi = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.student.ism} {self.student.familiya} ({self.shartnoma_raqami}, {self.status})"


