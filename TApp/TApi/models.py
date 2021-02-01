from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

class TortoiseBaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class TortoiseSharableBaseModel(TortoiseBaseModel):
    SHARE_MEDIA_TYPE_IMAGE = 'image'
    SHARE_MEDIA_TYPE_VIDEO = 'video'

    _SHARE_MEDIA_TYPE_CHOICES = [
        (SHARE_MEDIA_TYPE_IMAGE, SHARE_MEDIA_TYPE_IMAGE),
        (SHARE_MEDIA_TYPE_VIDEO, SHARE_MEDIA_TYPE_VIDEO)
    ]

    SHARE_MEDIA_EXTENSION_MP4 = 'mp4'
    SHARE_MEDIA_EXTENSION_PNG = 'png'
    SHARE_MEDIA_EXTENSION_JPG = 'jpg'
    SHARE_MEDIA_EXTENSION_JPEG = 'jpeg'
    SHARE_MEDIA_EXTENSION_GIF = 'gif'

    _SHARE_MEDIA_EXTENSION_CHOICES = [
        (SHARE_MEDIA_EXTENSION_MP4, SHARE_MEDIA_EXTENSION_MP4),
        (SHARE_MEDIA_EXTENSION_PNG, SHARE_MEDIA_EXTENSION_PNG),
        (SHARE_MEDIA_EXTENSION_JPG, SHARE_MEDIA_EXTENSION_JPG),
        (SHARE_MEDIA_EXTENSION_JPEG, SHARE_MEDIA_EXTENSION_JPEG),
        (SHARE_MEDIA_EXTENSION_GIF, SHARE_MEDIA_EXTENSION_GIF)
    ]

    share_media_url = models.URLField()
    share_text = models.TextField()
    share_media_type = models.CharField(choices=_SHARE_MEDIA_TYPE_CHOICES, max_length=8)
    share_media_extension = models.CharField(choices=_SHARE_MEDIA_EXTENSION_CHOICES, max_length=6)

    class Meta:
        abstract = True

class UserProfile(TortoiseBaseModel):
    USER_STATUS_ACTIVE = 'active'
    USER_STATUS_VERIFIED = 'verified'
    USER_STATUS_PENDING = 'pending'

    _USER_STATUS_CHOICES = [
        (USER_STATUS_ACTIVE, USER_STATUS_ACTIVE),
        (USER_STATUS_VERIFIED, USER_STATUS_VERIFIED),
        (USER_STATUS_PENDING, USER_STATUS_PENDING)
    ]
    
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_OTHER = 'other'

    _GENDER_CHOICES = [
        (GENDER_MALE, GENDER_MALE),
        (GENDER_FEMALE, GENDER_FEMALE),
        (GENDER_OTHER, GENDER_OTHER)
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)
    user_status = models.CharField(choices=_USER_STATUS_CHOICES, max_length=10, default=USER_STATUS_ACTIVE)
    pincode = models.CharField(max_length=6, null=True)
    gender = models.CharField(choices=_GENDER_CHOICES, max_length=8, null=True)
    dob = models.DateTimeField(null=True)
    upi_address = models.CharField(max_length=128, null=True)
    reward_balance = models.IntegerField(default=0)
    fcm_token = models.CharField(max_length=256)

class RewardHistory(TortoiseBaseModel):
    TRANSACTION_TYPE_CREDITED = 'credited'
    TRANSACTION_TYPE_DEBITED = 'debited'
    _TRANSACTION_TYPE_CHOICES = [
        (TRANSACTION_TYPE_CREDITED, TRANSACTION_TYPE_CREDITED),
        (TRANSACTION_TYPE_DEBITED, TRANSACTION_TYPE_DEBITED)
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=8, choices=_TRANSACTION_TYPE_CHOICES)
    transaction_value = models.IntegerField()
    current_user_rewards = models.IntegerField()

class Merchant(TortoiseBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=13)
    address = models.TextField()
    logo_url = models.URLField()

    def __str__(self):
        return self.user.id

class Category(TortoiseBaseModel):
    title = models.CharField(max_length=32)
    description = models.TextField()
    img_url = models.URLField()
    color = models.CharField(max_length=7)
    gradient_color = models.CharField(max_length=7)

class ProcessInfo(TortoiseBaseModel):
    caption = models.TextField()

class ProcessInfoSteps(TortoiseBaseModel):
    sno = models.IntegerField()
    has_explanation = models.BooleanField()
    explanation_text = models.TextField()
    explanation_description = models.TextField()
    process_info = models.ForeignKey(ProcessInfo, on_delete=models.CASCADE)

class ProcessStepDescription(TortoiseBaseModel):
    STYLE_NONE = 'none'
    STYLE_UNDERLINE = 'underline'
    STYLE_BOLD = 'bold'

    _STYLE_CHOICES = [
        (STYLE_NONE, STYLE_NONE),
        (STYLE_BOLD, STYLE_BOLD),
        (STYLE_UNDERLINE, STYLE_UNDERLINE)
    ]

    sno = models.IntegerField()
    text = models.TextField()
    style = models.CharField(choices=_STYLE_CHOICES, max_length=10)
    process_info_steps = models.ForeignKey(ProcessInfoSteps, on_delete=models.CASCADE)

class RedemptionInfo(TortoiseBaseModel):
    caption = models.TextField()
    terms_on_display = models.IntegerField(default=4)

class RedemptionInfoItem(TortoiseBaseModel):
    sno = models.IntegerField()
    text = models.TextField()
    redemption_info = models.ForeignKey(RedemptionInfo, on_delete=models.CASCADE)

class CancellationInfo(TortoiseBaseModel):
    caption = models.TextField()
    terms_on_display = models.IntegerField(default=4)

class CancellationInfoItem(TortoiseBaseModel):
    sno = models.IntegerField()
    text = models.TextField()
    cancellation_info = models.ForeignKey(CancellationInfo, on_delete=models.CASCADE)

class TermsInfo(TortoiseBaseModel):
    caption = models.TextField()
    terms_on_display = models.IntegerField(default=4)

class TermsInfoItem(TortoiseBaseModel):
    sno = models.IntegerField()
    description = models.TextField()
    terms_info = models.ForeignKey(TermsInfo, on_delete=models.CASCADE)

class Scheme(TortoiseSharableBaseModel):
    PROMOTION_TYPE_TRENDING = 'trending'
    PROMOTION_TYPE_USER_NUMBER = 'userNumber'
    PROMOTION_TYPE_RECOMMENDED = 'recommended'
    PROMOTION_TYPE_POPULAR = 'popular'
    PROMOTION_TYPE_ANSWER_TO_WIN = 'answerToWin'
    _PROMOTION_TYPE_CHOICES = [
        (PROMOTION_TYPE_ANSWER_TO_WIN, PROMOTION_TYPE_ANSWER_TO_WIN),
        (PROMOTION_TYPE_POPULAR, PROMOTION_TYPE_POPULAR),
        (PROMOTION_TYPE_RECOMMENDED, PROMOTION_TYPE_RECOMMENDED),
        (PROMOTION_TYPE_TRENDING, PROMOTION_TYPE_TRENDING),
        (PROMOTION_TYPE_USER_NUMBER, PROMOTION_TYPE_USER_NUMBER)
    ]

    AVAILABILITY_STATUS_DRAFT = 'draft'
    AVAILABILITY_STATUS_DISABLED = 'disabled'
    AVAILABILITY_STATUS_ACTIVE = 'active'
    _AVAILABILITY_STATUS_CHOICES = [
        (AVAILABILITY_STATUS_DRAFT, AVAILABILITY_STATUS_DRAFT),
        (AVAILABILITY_STATUS_DISABLED, AVAILABILITY_STATUS_DISABLED),
        (AVAILABILITY_STATUS_ACTIVE, AVAILABILITY_STATUS_ACTIVE)
    ]

    uuid = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=128)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    availability_status = models.CharField(max_length=16, choices=_AVAILABILITY_STATUS_CHOICES)
    cover_photo_url = models.URLField()
    caption = models.TextField()
    whats_this_title = models.CharField(max_length=256)
    whats_this_description = models.TextField()
    min_amt = models.IntegerField()
    max_amt = models.IntegerField()
    multiplier = models.IntegerField()
    allow_custom_amt = models.BooleanField()
    total_users = models.IntegerField(default=0)
    terms = models.OneToOneField(TermsInfo, on_delete=models.CASCADE)
    redemption_terms = models.OneToOneField(RedemptionInfo, on_delete=models.CASCADE)
    cancellation_terms = models.OneToOneField(CancellationInfo, on_delete=models.CASCADE)
    is_verified = models.BooleanField()
    verified_title = models.CharField(max_length=128)
    verified_caption = models.TextField()
    verified_hyper_text = models.CharField(max_length=128)
    verified_hyper_link = models.URLField()
    verified_merchant_icon = models.URLField()
    is_promoted = models.BooleanField()
    promotion_type = models.CharField(choices=_PROMOTION_TYPE_CHOICES, null=True, max_length=16)
    promotion_text = models.CharField(max_length=128)
    faqs_on_display = models.IntegerField(default=4)

class BenefitsInfo(TortoiseBaseModel):
    sno = models.IntegerField()
    description = models.TextField()
    icon_url = models.URLField()
    scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE)

class QuickAnswer(TortoiseBaseModel):
    sno = models.IntegerField()
    question = models.TextField()
    answer = models.TextField()
    scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE)

class FaqForScheme(TortoiseBaseModel):
    sno = models.IntegerField()
    question = models.TextField()
    answer = models.TextField()
    scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE)

class TenureForScheme(TortoiseBaseModel):
    duration = models.IntegerField()
    caption = models.CharField(max_length=128)
    downpayment = models.IntegerField(default=0)
    redeem_from = models.IntegerField()
    redeem_till = models.IntegerField()
    scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE)

class InstalmentOptionForTenure(TortoiseBaseModel):
    tenure = models.ForeignKey(TenureForScheme, on_delete=models.CASCADE)
    amount = models.IntegerField()

class PortfolioImages(TortoiseBaseModel):
    sno = models.IntegerField()
    image_url = models.URLField()
    scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE)

class SchemeReviews(TortoiseBaseModel):
    timestamp = models.DateTimeField()
    username = models.CharField(max_length=64)
    user_photo = models.URLField()
    review = models.TextField()
    scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE)

class Plan(TortoiseBaseModel):
    PLAN_STATUS_KYC_PENDING = 'kycPending'
    PLAN_STATUS_ACTIVE = 'active'
    PLAN_STATUS_CANCELLED = 'cancelled'
    PLAN_STATUS_COMPLETED = 'completed'
    PLAN_STATUS_REDEEMED = 'redeemed'
    PLAN_STATUS_REFUND_INITIATED = 'refundInitiated'
    PLAN_STATUS_REFUND_COMPLETED = 'refundCompleted'
    PLAN_STATUS_VOIDED = 'voided'
    _PLAN_STATUS_CHOICES = [
        (PLAN_STATUS_KYC_PENDING, PLAN_STATUS_KYC_PENDING),
        (PLAN_STATUS_ACTIVE, PLAN_STATUS_ACTIVE),
        (PLAN_STATUS_CANCELLED, PLAN_STATUS_CANCELLED),
        (PLAN_STATUS_COMPLETED, PLAN_STATUS_COMPLETED),
        (PLAN_STATUS_REDEEMED, PLAN_STATUS_REDEEMED),
        (PLAN_STATUS_REFUND_INITIATED, PLAN_STATUS_REFUND_INITIATED),
        (PLAN_STATUS_REFUND_COMPLETED, PLAN_STATUS_REFUND_COMPLETED),
        (PLAN_STATUS_VOIDED, PLAN_STATUS_VOIDED)
    ]

    PLAN_PAYMENT_STATUS_OVERDUE = 'overdue'
    PLAN_PAYMENT_STATUS_PAY_NOW = 'paynow'
    PLAN_PAYMENT_STATUS_PAID = 'paid'
    PLAN_PAYMENT_STATUS_MISSED = 'missed'
    PLAN_PAYMENT_STATUS_RESUMED = 'resumed'
    PLAN_PAYMENT_STATUS_NO_PAYMENTS_YET = 'nopaymentsyet'
    _PLAN_PAYMENT_STATUS_CHOICES = [
        (PLAN_PAYMENT_STATUS_MISSED, PLAN_PAYMENT_STATUS_MISSED),
        (PLAN_PAYMENT_STATUS_NO_PAYMENTS_YET, PLAN_PAYMENT_STATUS_NO_PAYMENTS_YET),
        (PLAN_PAYMENT_STATUS_OVERDUE, PLAN_PAYMENT_STATUS_OVERDUE),
        (PLAN_PAYMENT_STATUS_PAY_NOW, PLAN_PAYMENT_STATUS_PAY_NOW),
        (PLAN_PAYMENT_STATUS_RESUMED, PLAN_PAYMENT_STATUS_RESUMED),
        (PLAN_PAYMENT_STATUS_PAID, PLAN_PAYMENT_STATUS_PAID)
    ]

    REDEMPTION_STATUS_CLOSING_SOON = 'closingSoon'
    REDEMPTION_STATUS_PLAN_COMPLETED = 'planCompleted'
    REDEMPTION_STATUS_PLAN_REDEEMED = 'planRedeemed'
    REDEMPTION_STATUS_OPEN = 'open'
    REDEMPTION_STATUS_NOT_AVAILABLE = 'notavailable'
    REDEMPTION_STATUS_CLOSED = 'closed'
    _REDEMPTION_STATUS_CHOICES = [
        (REDEMPTION_STATUS_CLOSING_SOON, REDEMPTION_STATUS_CLOSING_SOON),
        (REDEMPTION_STATUS_CLOSED, REDEMPTION_STATUS_CLOSED),
        (REDEMPTION_STATUS_NOT_AVAILABLE, REDEMPTION_STATUS_NOT_AVAILABLE),
        (REDEMPTION_STATUS_OPEN, REDEMPTION_STATUS_OPEN),
        (REDEMPTION_STATUS_PLAN_COMPLETED, REDEMPTION_STATUS_PLAN_COMPLETED),
        (REDEMPTION_STATUS_PLAN_REDEEMED, REDEMPTION_STATUS_PLAN_REDEEMED),
    ]

    BONUS_STATUS_SAME = 'same'
    BONUS_STATUS_INCREASED = 'increased'
    BONUS_STATUS_DECREASED = 'decreased'
    _BONUS_STATUS_CHOICES = [
        (BONUS_STATUS_SAME, BONUS_STATUS_SAME),
        (BONUS_STATUS_INCREASED, BONUS_STATUS_INCREASED),
        (BONUS_STATUS_DECREASED, BONUS_STATUS_DECREASED)
    ]

    uuid = models.CharField(max_length=6, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE)
    plan_status = models.CharField(choices=_PLAN_STATUS_CHOICES, max_length=18)
    start_date = models.DateTimeField()
    instalment_amount = models.IntegerField()
    plan_amount = models.IntegerField()
    total_paid_amount = models.IntegerField()
    next_instalment_date = models.DateTimeField()
    completed_instalments = models.IntegerField(default=0)
    total_instalments = models.IntegerField()
    penalties = models.IntegerField()
    plan_complete_date = models.DateTimeField()
    redemption_last_date = models.DateTimeField()
    redeemed_on = models.DateTimeField(null=True)
    current_cancellation_amount = models.IntegerField()
    payment_status = models.CharField(choices=_PLAN_PAYMENT_STATUS_CHOICES,max_length=16)
    redemption_status = models.CharField(choices=_REDEMPTION_STATUS_CHOICES, max_length=16)
    bonus_status = models.CharField(choices=_BONUS_STATUS_CHOICES, max_length=12)

    def get_payment_history(self):
        pass

    def __str__(self):
        return '%s %s %s %s' % (self.user, self.plan_status, self.uuid, self.total_paid_amount)

class Instalment(TortoiseBaseModel):
    INSTALMENT_STATUS_PAID = 'paid'
    INSTALMENT_STATUS_MISSED = 'missed'
    INSTALMENT_STATUS_OVERDUE = 'overdue'
    INSTALMENT_STATUS_NEXT = 'next'
    INSTALMENT_STATUS_UPCOMING = 'upcoming'
    _INSTALMENT_STATUS_CHOICES = [
        (INSTALMENT_STATUS_PAID, INSTALMENT_STATUS_PAID),
        (INSTALMENT_STATUS_MISSED, INSTALMENT_STATUS_MISSED),
        (INSTALMENT_STATUS_OVERDUE, INSTALMENT_STATUS_OVERDUE),
        (INSTALMENT_STATUS_NEXT, INSTALMENT_STATUS_NEXT),
        (INSTALMENT_STATUS_UPCOMING, INSTALMENT_STATUS_UPCOMING)
    ]

    sno = models.IntegerField()
    due_date = models.DateTimeField()
    paid_date = models.DateTimeField(null=True)
    status = models.CharField(choices=_INSTALMENT_STATUS_CHOICES, max_length=10)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    def get_latest_payment(self):
        pass

class Payment(TortoiseBaseModel):
    PAYMENT_STATUS_PROCESSING = 'processing'
    PAYMENT_STATUS_RECEIVED = 'received'
    PAYMENT_STATUS_FAILED = 'failed'
    _PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PROCESSING, PAYMENT_STATUS_PROCESSING),
        (PAYMENT_STATUS_RECEIVED, PAYMENT_STATUS_RECEIVED),
        (PAYMENT_STATUS_FAILED, PAYMENT_STATUS_FAILED)
    ]

    uuid = models.CharField(max_length=8)
    amount = models.IntegerField()
    status = models.CharField(choices=_PAYMENT_STATUS_CHOICES, max_length=12)
    invoice_url = models.URLField()
    instalment = models.ForeignKey(Instalment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

class RedemptionBonus(TortoiseBaseModel):
    BONUS_AT_PLAN_ENROLMENT = 'planEnrolment'
    BONUS_AT_PRESENT = 'currentPlanBonus'
    BONUS_AT_SCHEME_OFFERING = 'schemeOffering'
    _BONUS_AT_CHOICES = [
        (BONUS_AT_PLAN_ENROLMENT, BONUS_AT_PLAN_ENROLMENT),
        (BONUS_AT_PRESENT, BONUS_AT_PRESENT),
        (BONUS_AT_SCHEME_OFFERING, BONUS_AT_SCHEME_OFFERING)
    ]

    BONUS_TYPE_VOUCHER = 'voucher'
    BONUS_TYPE_CREDITS = 'credits'
    _BONUS_TYPE_CHOICES = [
        (BONUS_TYPE_VOUCHER, BONUS_TYPE_VOUCHER),
        (BONUS_TYPE_CREDITS, BONUS_TYPE_CREDITS)
    ]

    sno = models.IntegerField()
    bonus_type = models.CharField(choices=_BONUS_TYPE_CHOICES, max_length=10)
    amount = models.IntegerField()
    name = models.CharField(max_length=100)
    return_pct = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    caption = models.TextField()
    bonus_at = models.CharField(choices=_BONUS_AT_CHOICES, max_length=18)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)
    instalment_scheme = models.ForeignKey(InstalmentOptionForTenure, on_delete=models.CASCADE)

class TortoiseTip(TortoiseSharableBaseModel):
    TIP_TYPE_ICON = 'icon'
    TIP_TYPE_IMAGE = 'image'
    _TIP_TYPE_CHOICES = [
        (TIP_TYPE_ICON, TIP_TYPE_ICON),
        (TIP_TYPE_IMAGE, TIP_TYPE_IMAGE)
    ]

    uuid = models.CharField(max_length=8, primary_key=True)
    image_url = models.URLField()
    header = models.CharField(max_length=64)
    caption = models.TextField()
    tip_type = models.CharField(choices=_TIP_TYPE_CHOICES, max_length=8)

class TipItem(TortoiseBaseModel):
    sno = models.IntegerField()
    header = models.CharField(max_length=128)
    content = models.TextField()
    tortoiseTip = models.ForeignKey(TortoiseTip, on_delete=models.CASCADE)

class DefaultCategoryFeed(TortoiseBaseModel):
    CARD_TYPE_SCHEME = 'scheme'
    CARD_TYPE_TIP = 'tip'
    CARD_TYPE_DESIRED_BRANDS = 'desiredBrands'
    CARD_TYPE_PARTNER_INFO = 'partnerInfo'
    CARD_TYPE_SCRATCH_CARD = 'scratchCard'
    CARD_TYPE_INTRO_CARD = 'introCard'
    CARD_TYPE_NO_SCHEMES = 'noSchemes'
    CARD_TYPE_PAYMENT_REMINDER = 'paymentReminder'

    _CARD_TYPE_CHOICES = [
        (CARD_TYPE_SCHEME, CARD_TYPE_SCHEME),
        (CARD_TYPE_TIP, CARD_TYPE_TIP),
        (CARD_TYPE_DESIRED_BRANDS, CARD_TYPE_DESIRED_BRANDS),
        (CARD_TYPE_PARTNER_INFO, CARD_TYPE_PARTNER_INFO),
        (CARD_TYPE_SCRATCH_CARD, CARD_TYPE_SCRATCH_CARD),
        (CARD_TYPE_INTRO_CARD, CARD_TYPE_INTRO_CARD),
        (CARD_TYPE_NO_SCHEMES, CARD_TYPE_NO_SCHEMES),
        (CARD_TYPE_PAYMENT_REMINDER, CARD_TYPE_PAYMENT_REMINDER)
    ]

    sno = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    card_type = models.CharField(max_length=18, choices=_CARD_TYPE_CHOICES)
    scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE, null=True, default=None)
    tip = models.ForeignKey(TortoiseTip, on_delete=models.CASCADE, null=True, default=None)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True, default=None)

class DefaultHomeFeed(TortoiseBaseModel):
    CARD_TYPE_SCHEME = 'scheme'
    CARD_TYPE_TIP = 'tip'
    CARD_TYPE_DESIRED_BRANDS = 'desiredBrands'
    CARD_TYPE_CATEGORIES = 'categories'
    CARD_TYPE_PARTNER_INFO = 'partnerInfo'
    CARD_TYPE_SCRATCH_CARD = 'scratchCard'
    CARD_TYPE_INTRO_CARD = 'introCard'
    CARD_TYPE_NO_SCHEMES = 'noSchemes'
    CARD_TYPE_PAYMENT_REMINDER = 'paymentReminder'

    _CARD_TYPE_CHOICES = [
        (CARD_TYPE_SCHEME, CARD_TYPE_SCHEME),
        (CARD_TYPE_TIP, CARD_TYPE_TIP),
        (CARD_TYPE_DESIRED_BRANDS, CARD_TYPE_DESIRED_BRANDS),
        (CARD_TYPE_PARTNER_INFO, CARD_TYPE_PARTNER_INFO),
        (CARD_TYPE_SCRATCH_CARD, CARD_TYPE_SCRATCH_CARD),
        (CARD_TYPE_CATEGORIES, CARD_TYPE_CATEGORIES),
        (CARD_TYPE_INTRO_CARD, CARD_TYPE_INTRO_CARD),
        (CARD_TYPE_NO_SCHEMES, CARD_TYPE_NO_SCHEMES),
        (CARD_TYPE_PAYMENT_REMINDER, CARD_TYPE_PAYMENT_REMINDER)
    ]

    sno = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, default=None)
    card_type = models.CharField(max_length=18, choices=_CARD_TYPE_CHOICES)
    scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE, null=True, default=None)
    tip = models.ForeignKey(TortoiseTip, on_delete=models.CASCADE, null=True, default=None)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True, default=None)


class UserHomeFeed(DefaultHomeFeed):
    user = models.ForeignKey(User, on_delete=models.CASCADE)