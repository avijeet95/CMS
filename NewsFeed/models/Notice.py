from django.db import models
from Course.models import Degree, Branch, Department


class NoticeManager(models.Manager):
    def addNotice(self, request):
        """ adds new notice """
        """ note: filelink, degree, branch, department are optional """
        N = Notice(
            subject=request['subject'],
            issuingAuthority=request['issuingAuthority'],
            fileLink=request['fileLink'],
        )

        if "degreeCode" and "degreeType" in request.keys():
            N.degree = Degree.objects.getDegreeByCodeAndType(request)
        if "branchCode" in request.keys():
            N.branch = Branch.objects.getBranchByCode(request)
        if "deptId" in request.keys():
            N.department = Department.objects.getDepartmentById(request)

        N.save()
        return N

    def getNoticeById(self, request):
        """ get notice details based on notice id """
        N = Notice.objects.get(id=request['id'])
        return N

    def retrieveNoticeById(self, request):
        pass

    def deleteNotice(self, request):
        """ deletes an existing notice """
        N = Notice.objects.get(id=request['id'])
        N = N.delete()
        return N


class Notice(models.Model):
    # Subject
    subject = models.CharField(max_length=250, blank=False, null=False)
    # IssuingAuthority
    issuingAuthority = models.CharField(max_length=250, blank=False, null=False)
    # Issue date
    issueDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    # Link of the file from DropBox
    fileLink = models.URLField(null=False, blank=False, default=False)
    # degree
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, null=True, blank=True)
    # branch
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    # department
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)

    objects = NoticeManager()

    def __str__(self):
        return self.subject
