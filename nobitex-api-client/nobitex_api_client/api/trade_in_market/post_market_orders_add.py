from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_market_orders_add_body import PostMarketOrdersAddBody
from ...models.post_market_orders_add_response_200 import PostMarketOrdersAddResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: PostMarketOrdersAddBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/market/orders/add",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostMarketOrdersAddResponse200]:
    if response.status_code == 200:
        response_200 = PostMarketOrdersAddResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostMarketOrdersAddResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMarketOrdersAddBody,
) -> Response[PostMarketOrdersAddResponse200]:
    """Add order

     ## ثبت سفارش

    برای ثبت سفارش معامله در بازار نوبیتکس از این درخواست استفاده نمایید.

    ثبت سفارش الزاماً به معنی انجام معامله نیست و بسته به نوع و قیمت سفارش و وضعیت لحظه‌ای بازار ممکن
    است معامله انجام شود یا نشود. با درخواست «وضعیت سفارش» می‌توانید از وضعیت سفارش خود مطلع شوید.

    مقادیر نوع سفارش:

    *   `sell`: خرید
    *   `buy`: فروش


    مقادیر حالت سفارش:

    *   `default`: عادی (تک سفارش)
    *   `oco`: OCO (دو سفارش همزمان)


    مقادیر نحوه اجرای سفارش:

    *   `limit`: با قیمت معین
    *   `market`: با قیمت بازار
        منظور سفارشی است که کاربر درخواست دارد تا به بهترین قیمت موجود بازار مورد انجام قرار گیرد.
    *   `stop_market`: حد ضرر
    *   `stop_limit`: حد ضرر معین
        این سفارش در زمان رسیدن قیمت بازار به قیمت توقف فعال خواهد شد. کاربرد اصلی آن، جلوگیری از زیان
    در صورت تغییر غیرمنتظره قیمت بازار است.


    رمزارزهای مبدا پشتیبانی شده:
    {{crypto_currencies}}

    ارزهای مقصد پشتیبانی شده:
    rls, usdt

    ### حالت‌های خطا

    در صورتی که درخواست ثبت سفارش معتبر نباشد، ممکن است یکی از این خطاها برگردانده شود. در این صورت
    سفارش شما ثبت نشده است و در صورت تمایل باید دوباره درخواست دهید.

    | کد خطا | توضیحات |
    | --- | --- |
    | InvalidOrderPrice | قیمت سفارش (price) تعیین نشده یا اشتباه است |
    | BadPrice | در سفارش عادی: قیمت تعیین شده برای سفارش نسبت به قیمت فعلی بازار تفاوت زیادی دارد. قیمت
    سفارش خود را در بازه‌ی ۳۰٪ قیمت کنونی بازار تعیین کنید.  <br>در سفارش حد ضرر: قیمت تعیین شده برای
    سفارش بازار نمی‌تواند از قیمت توقف بهتر باشد.  <br>در سفارش OCO: قیمت و قیمت توقف تعیین شده برای
    سفارش حد ضرر نمی‌تواند از قیمت سفارش با قیمت معین بهتر باشد. |
    | InvalidExecutionType | نوع:مارکت/لیمیت اجرای سفارش (execution) تعیین نشده یا اشتباه است. |
    | InvalidOrderType | نوع:خرید/فروش سفارش (type) تعیین نشده یا اشتباه است. |
    | OverValueOrder | مقدار سفارش فروش (amount) یا ارزش کل سفارش خرید (amount*price) از موجودی کیف پول
    نوبیتکس شما کمتر است. |
    | SmallOrder | حداقل ارزش معامله رعایت نشده است. حداقل ارزش معامله برای بازارهای ریالی، 3 میلیون
    ریال و برای بازارهای تتری، ۱۱ تتر است و مبلغ کل سفارش  <br>(amount*price) باید بیشتر از این حداقل
    باشد. |
    | DuplicateOrder | سفارشی با همین مشخصات توسط کاربر شما در بازه زمانی ده ثانیه اخیر ارسال شده است. |
    | InvalidMarketPair | رمزارز مبدا (srcCurrency) یا رمزارز مقصد (dstCurrency) به درستی مقداردهی نشده
    است یا چنین بازاری در نوبیتکس وجود ندارد. |
    | MarketClosed | بازار مد نظر در حال حاضر به صورت موقت بسته است. |
    | TradingUnavailable | کاربر اجازه‌ی معامله ندارد، فرآیند احراز هویت خود را تکمیل نمایید. |
    | FeatureUnavailable | شما از کاربران مجاز به استفاده از امکانات آزمایشی نیستید. |

    ### نکات و ملاحظات

    1.  **محدودیت فراخوانی:** ۱۰۰ درخواست در هر ۱۰ دقیقه
    2.  **واحدها:** واحد قیمت در بازارهای ریالی به ریال (و نه تومان) می‌باشد. واحد قیمت در بازارهای تتری
    نیز تتر می‌باشد. واحد پارامتر مقدار (amount) بر حسب رمزارز مبدا (srcCurrency) است.
    3.  **تعیین محدوده مورد انتظار قیمت:** در سفارش‌های مارکت به شدت توصیه می‌شود که پارامتر price را
    نیز مشخص نمایید. این پارامتر در سفارش مارکت تخمین شما از قیمت بازار را نمایش می‌دهد و باعث می‌شود
    سفارش شما تنها تا جایی پر شود که قیمت معامله در بازه‌ی قیمتی مشخص شده باشد. برای پیش‌گیری از معاملات
    با قیمت ناخواسته به علت نوسانات دفعی بازار، پیشنهاد می‌شود که حتماً قیمت تقریبی مد نظر خود را در
    سفارش‌های مارکت نیز ارسال کنید. اگر پارامتر price را ارسال ننمایید، معامله با قیمت لحظه‌ای بازار (یا
    قیمت توقف در سفارش‌های حد ضرر) تا بازه نوسان ۱٪، انجام خواهد شد.
    4.  **سفارش تکراری:** برای جلوگیری از ثبت سفارش تکراری ناشی از اختلالات شبکه و سرور، در صورتی که دو
    سفارش با پارامترهای ورودی کاملاً مشابه از جمله نوع و قیمت و مقدار، در بازه‌ی زمانی کمتر از ده ثانیه
    ارسال نمایید، تنها سفارش اول پذیرفته می‌شود. (غیرفعال در حالت Pro)
    5.  **دقت مقادیر پولی (monetary):** نوع monetary که در ارامترهای `amount` و `price` به کار می‌رود،
    بسته به بازار هر رمزارز، تعداد رقم اعشار متغیری بین ۰ تا ۸ رقم دارد. در صورت ارسال مقادیر با ارقام
    اعشاری بیشتر، ارقام بی‌معنی
        در مقدار به پایین و در قیمت به روش بانکداری گرد خواهند شد.
        [مشاهده جدول دقت‌ها](https://nobitex.ir/policies/markets/)

    Args:
        body (PostMarketOrdersAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostMarketOrdersAddResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMarketOrdersAddBody,
) -> Optional[PostMarketOrdersAddResponse200]:
    """Add order

     ## ثبت سفارش

    برای ثبت سفارش معامله در بازار نوبیتکس از این درخواست استفاده نمایید.

    ثبت سفارش الزاماً به معنی انجام معامله نیست و بسته به نوع و قیمت سفارش و وضعیت لحظه‌ای بازار ممکن
    است معامله انجام شود یا نشود. با درخواست «وضعیت سفارش» می‌توانید از وضعیت سفارش خود مطلع شوید.

    مقادیر نوع سفارش:

    *   `sell`: خرید
    *   `buy`: فروش


    مقادیر حالت سفارش:

    *   `default`: عادی (تک سفارش)
    *   `oco`: OCO (دو سفارش همزمان)


    مقادیر نحوه اجرای سفارش:

    *   `limit`: با قیمت معین
    *   `market`: با قیمت بازار
        منظور سفارشی است که کاربر درخواست دارد تا به بهترین قیمت موجود بازار مورد انجام قرار گیرد.
    *   `stop_market`: حد ضرر
    *   `stop_limit`: حد ضرر معین
        این سفارش در زمان رسیدن قیمت بازار به قیمت توقف فعال خواهد شد. کاربرد اصلی آن، جلوگیری از زیان
    در صورت تغییر غیرمنتظره قیمت بازار است.


    رمزارزهای مبدا پشتیبانی شده:
    {{crypto_currencies}}

    ارزهای مقصد پشتیبانی شده:
    rls, usdt

    ### حالت‌های خطا

    در صورتی که درخواست ثبت سفارش معتبر نباشد، ممکن است یکی از این خطاها برگردانده شود. در این صورت
    سفارش شما ثبت نشده است و در صورت تمایل باید دوباره درخواست دهید.

    | کد خطا | توضیحات |
    | --- | --- |
    | InvalidOrderPrice | قیمت سفارش (price) تعیین نشده یا اشتباه است |
    | BadPrice | در سفارش عادی: قیمت تعیین شده برای سفارش نسبت به قیمت فعلی بازار تفاوت زیادی دارد. قیمت
    سفارش خود را در بازه‌ی ۳۰٪ قیمت کنونی بازار تعیین کنید.  <br>در سفارش حد ضرر: قیمت تعیین شده برای
    سفارش بازار نمی‌تواند از قیمت توقف بهتر باشد.  <br>در سفارش OCO: قیمت و قیمت توقف تعیین شده برای
    سفارش حد ضرر نمی‌تواند از قیمت سفارش با قیمت معین بهتر باشد. |
    | InvalidExecutionType | نوع:مارکت/لیمیت اجرای سفارش (execution) تعیین نشده یا اشتباه است. |
    | InvalidOrderType | نوع:خرید/فروش سفارش (type) تعیین نشده یا اشتباه است. |
    | OverValueOrder | مقدار سفارش فروش (amount) یا ارزش کل سفارش خرید (amount*price) از موجودی کیف پول
    نوبیتکس شما کمتر است. |
    | SmallOrder | حداقل ارزش معامله رعایت نشده است. حداقل ارزش معامله برای بازارهای ریالی، 3 میلیون
    ریال و برای بازارهای تتری، ۱۱ تتر است و مبلغ کل سفارش  <br>(amount*price) باید بیشتر از این حداقل
    باشد. |
    | DuplicateOrder | سفارشی با همین مشخصات توسط کاربر شما در بازه زمانی ده ثانیه اخیر ارسال شده است. |
    | InvalidMarketPair | رمزارز مبدا (srcCurrency) یا رمزارز مقصد (dstCurrency) به درستی مقداردهی نشده
    است یا چنین بازاری در نوبیتکس وجود ندارد. |
    | MarketClosed | بازار مد نظر در حال حاضر به صورت موقت بسته است. |
    | TradingUnavailable | کاربر اجازه‌ی معامله ندارد، فرآیند احراز هویت خود را تکمیل نمایید. |
    | FeatureUnavailable | شما از کاربران مجاز به استفاده از امکانات آزمایشی نیستید. |

    ### نکات و ملاحظات

    1.  **محدودیت فراخوانی:** ۱۰۰ درخواست در هر ۱۰ دقیقه
    2.  **واحدها:** واحد قیمت در بازارهای ریالی به ریال (و نه تومان) می‌باشد. واحد قیمت در بازارهای تتری
    نیز تتر می‌باشد. واحد پارامتر مقدار (amount) بر حسب رمزارز مبدا (srcCurrency) است.
    3.  **تعیین محدوده مورد انتظار قیمت:** در سفارش‌های مارکت به شدت توصیه می‌شود که پارامتر price را
    نیز مشخص نمایید. این پارامتر در سفارش مارکت تخمین شما از قیمت بازار را نمایش می‌دهد و باعث می‌شود
    سفارش شما تنها تا جایی پر شود که قیمت معامله در بازه‌ی قیمتی مشخص شده باشد. برای پیش‌گیری از معاملات
    با قیمت ناخواسته به علت نوسانات دفعی بازار، پیشنهاد می‌شود که حتماً قیمت تقریبی مد نظر خود را در
    سفارش‌های مارکت نیز ارسال کنید. اگر پارامتر price را ارسال ننمایید، معامله با قیمت لحظه‌ای بازار (یا
    قیمت توقف در سفارش‌های حد ضرر) تا بازه نوسان ۱٪، انجام خواهد شد.
    4.  **سفارش تکراری:** برای جلوگیری از ثبت سفارش تکراری ناشی از اختلالات شبکه و سرور، در صورتی که دو
    سفارش با پارامترهای ورودی کاملاً مشابه از جمله نوع و قیمت و مقدار، در بازه‌ی زمانی کمتر از ده ثانیه
    ارسال نمایید، تنها سفارش اول پذیرفته می‌شود. (غیرفعال در حالت Pro)
    5.  **دقت مقادیر پولی (monetary):** نوع monetary که در ارامترهای `amount` و `price` به کار می‌رود،
    بسته به بازار هر رمزارز، تعداد رقم اعشار متغیری بین ۰ تا ۸ رقم دارد. در صورت ارسال مقادیر با ارقام
    اعشاری بیشتر، ارقام بی‌معنی
        در مقدار به پایین و در قیمت به روش بانکداری گرد خواهند شد.
        [مشاهده جدول دقت‌ها](https://nobitex.ir/policies/markets/)

    Args:
        body (PostMarketOrdersAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostMarketOrdersAddResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMarketOrdersAddBody,
) -> Response[PostMarketOrdersAddResponse200]:
    """Add order

     ## ثبت سفارش

    برای ثبت سفارش معامله در بازار نوبیتکس از این درخواست استفاده نمایید.

    ثبت سفارش الزاماً به معنی انجام معامله نیست و بسته به نوع و قیمت سفارش و وضعیت لحظه‌ای بازار ممکن
    است معامله انجام شود یا نشود. با درخواست «وضعیت سفارش» می‌توانید از وضعیت سفارش خود مطلع شوید.

    مقادیر نوع سفارش:

    *   `sell`: خرید
    *   `buy`: فروش


    مقادیر حالت سفارش:

    *   `default`: عادی (تک سفارش)
    *   `oco`: OCO (دو سفارش همزمان)


    مقادیر نحوه اجرای سفارش:

    *   `limit`: با قیمت معین
    *   `market`: با قیمت بازار
        منظور سفارشی است که کاربر درخواست دارد تا به بهترین قیمت موجود بازار مورد انجام قرار گیرد.
    *   `stop_market`: حد ضرر
    *   `stop_limit`: حد ضرر معین
        این سفارش در زمان رسیدن قیمت بازار به قیمت توقف فعال خواهد شد. کاربرد اصلی آن، جلوگیری از زیان
    در صورت تغییر غیرمنتظره قیمت بازار است.


    رمزارزهای مبدا پشتیبانی شده:
    {{crypto_currencies}}

    ارزهای مقصد پشتیبانی شده:
    rls, usdt

    ### حالت‌های خطا

    در صورتی که درخواست ثبت سفارش معتبر نباشد، ممکن است یکی از این خطاها برگردانده شود. در این صورت
    سفارش شما ثبت نشده است و در صورت تمایل باید دوباره درخواست دهید.

    | کد خطا | توضیحات |
    | --- | --- |
    | InvalidOrderPrice | قیمت سفارش (price) تعیین نشده یا اشتباه است |
    | BadPrice | در سفارش عادی: قیمت تعیین شده برای سفارش نسبت به قیمت فعلی بازار تفاوت زیادی دارد. قیمت
    سفارش خود را در بازه‌ی ۳۰٪ قیمت کنونی بازار تعیین کنید.  <br>در سفارش حد ضرر: قیمت تعیین شده برای
    سفارش بازار نمی‌تواند از قیمت توقف بهتر باشد.  <br>در سفارش OCO: قیمت و قیمت توقف تعیین شده برای
    سفارش حد ضرر نمی‌تواند از قیمت سفارش با قیمت معین بهتر باشد. |
    | InvalidExecutionType | نوع:مارکت/لیمیت اجرای سفارش (execution) تعیین نشده یا اشتباه است. |
    | InvalidOrderType | نوع:خرید/فروش سفارش (type) تعیین نشده یا اشتباه است. |
    | OverValueOrder | مقدار سفارش فروش (amount) یا ارزش کل سفارش خرید (amount*price) از موجودی کیف پول
    نوبیتکس شما کمتر است. |
    | SmallOrder | حداقل ارزش معامله رعایت نشده است. حداقل ارزش معامله برای بازارهای ریالی، 3 میلیون
    ریال و برای بازارهای تتری، ۱۱ تتر است و مبلغ کل سفارش  <br>(amount*price) باید بیشتر از این حداقل
    باشد. |
    | DuplicateOrder | سفارشی با همین مشخصات توسط کاربر شما در بازه زمانی ده ثانیه اخیر ارسال شده است. |
    | InvalidMarketPair | رمزارز مبدا (srcCurrency) یا رمزارز مقصد (dstCurrency) به درستی مقداردهی نشده
    است یا چنین بازاری در نوبیتکس وجود ندارد. |
    | MarketClosed | بازار مد نظر در حال حاضر به صورت موقت بسته است. |
    | TradingUnavailable | کاربر اجازه‌ی معامله ندارد، فرآیند احراز هویت خود را تکمیل نمایید. |
    | FeatureUnavailable | شما از کاربران مجاز به استفاده از امکانات آزمایشی نیستید. |

    ### نکات و ملاحظات

    1.  **محدودیت فراخوانی:** ۱۰۰ درخواست در هر ۱۰ دقیقه
    2.  **واحدها:** واحد قیمت در بازارهای ریالی به ریال (و نه تومان) می‌باشد. واحد قیمت در بازارهای تتری
    نیز تتر می‌باشد. واحد پارامتر مقدار (amount) بر حسب رمزارز مبدا (srcCurrency) است.
    3.  **تعیین محدوده مورد انتظار قیمت:** در سفارش‌های مارکت به شدت توصیه می‌شود که پارامتر price را
    نیز مشخص نمایید. این پارامتر در سفارش مارکت تخمین شما از قیمت بازار را نمایش می‌دهد و باعث می‌شود
    سفارش شما تنها تا جایی پر شود که قیمت معامله در بازه‌ی قیمتی مشخص شده باشد. برای پیش‌گیری از معاملات
    با قیمت ناخواسته به علت نوسانات دفعی بازار، پیشنهاد می‌شود که حتماً قیمت تقریبی مد نظر خود را در
    سفارش‌های مارکت نیز ارسال کنید. اگر پارامتر price را ارسال ننمایید، معامله با قیمت لحظه‌ای بازار (یا
    قیمت توقف در سفارش‌های حد ضرر) تا بازه نوسان ۱٪، انجام خواهد شد.
    4.  **سفارش تکراری:** برای جلوگیری از ثبت سفارش تکراری ناشی از اختلالات شبکه و سرور، در صورتی که دو
    سفارش با پارامترهای ورودی کاملاً مشابه از جمله نوع و قیمت و مقدار، در بازه‌ی زمانی کمتر از ده ثانیه
    ارسال نمایید، تنها سفارش اول پذیرفته می‌شود. (غیرفعال در حالت Pro)
    5.  **دقت مقادیر پولی (monetary):** نوع monetary که در ارامترهای `amount` و `price` به کار می‌رود،
    بسته به بازار هر رمزارز، تعداد رقم اعشار متغیری بین ۰ تا ۸ رقم دارد. در صورت ارسال مقادیر با ارقام
    اعشاری بیشتر، ارقام بی‌معنی
        در مقدار به پایین و در قیمت به روش بانکداری گرد خواهند شد.
        [مشاهده جدول دقت‌ها](https://nobitex.ir/policies/markets/)

    Args:
        body (PostMarketOrdersAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostMarketOrdersAddResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMarketOrdersAddBody,
) -> Optional[PostMarketOrdersAddResponse200]:
    """Add order

     ## ثبت سفارش

    برای ثبت سفارش معامله در بازار نوبیتکس از این درخواست استفاده نمایید.

    ثبت سفارش الزاماً به معنی انجام معامله نیست و بسته به نوع و قیمت سفارش و وضعیت لحظه‌ای بازار ممکن
    است معامله انجام شود یا نشود. با درخواست «وضعیت سفارش» می‌توانید از وضعیت سفارش خود مطلع شوید.

    مقادیر نوع سفارش:

    *   `sell`: خرید
    *   `buy`: فروش


    مقادیر حالت سفارش:

    *   `default`: عادی (تک سفارش)
    *   `oco`: OCO (دو سفارش همزمان)


    مقادیر نحوه اجرای سفارش:

    *   `limit`: با قیمت معین
    *   `market`: با قیمت بازار
        منظور سفارشی است که کاربر درخواست دارد تا به بهترین قیمت موجود بازار مورد انجام قرار گیرد.
    *   `stop_market`: حد ضرر
    *   `stop_limit`: حد ضرر معین
        این سفارش در زمان رسیدن قیمت بازار به قیمت توقف فعال خواهد شد. کاربرد اصلی آن، جلوگیری از زیان
    در صورت تغییر غیرمنتظره قیمت بازار است.


    رمزارزهای مبدا پشتیبانی شده:
    {{crypto_currencies}}

    ارزهای مقصد پشتیبانی شده:
    rls, usdt

    ### حالت‌های خطا

    در صورتی که درخواست ثبت سفارش معتبر نباشد، ممکن است یکی از این خطاها برگردانده شود. در این صورت
    سفارش شما ثبت نشده است و در صورت تمایل باید دوباره درخواست دهید.

    | کد خطا | توضیحات |
    | --- | --- |
    | InvalidOrderPrice | قیمت سفارش (price) تعیین نشده یا اشتباه است |
    | BadPrice | در سفارش عادی: قیمت تعیین شده برای سفارش نسبت به قیمت فعلی بازار تفاوت زیادی دارد. قیمت
    سفارش خود را در بازه‌ی ۳۰٪ قیمت کنونی بازار تعیین کنید.  <br>در سفارش حد ضرر: قیمت تعیین شده برای
    سفارش بازار نمی‌تواند از قیمت توقف بهتر باشد.  <br>در سفارش OCO: قیمت و قیمت توقف تعیین شده برای
    سفارش حد ضرر نمی‌تواند از قیمت سفارش با قیمت معین بهتر باشد. |
    | InvalidExecutionType | نوع:مارکت/لیمیت اجرای سفارش (execution) تعیین نشده یا اشتباه است. |
    | InvalidOrderType | نوع:خرید/فروش سفارش (type) تعیین نشده یا اشتباه است. |
    | OverValueOrder | مقدار سفارش فروش (amount) یا ارزش کل سفارش خرید (amount*price) از موجودی کیف پول
    نوبیتکس شما کمتر است. |
    | SmallOrder | حداقل ارزش معامله رعایت نشده است. حداقل ارزش معامله برای بازارهای ریالی، 3 میلیون
    ریال و برای بازارهای تتری، ۱۱ تتر است و مبلغ کل سفارش  <br>(amount*price) باید بیشتر از این حداقل
    باشد. |
    | DuplicateOrder | سفارشی با همین مشخصات توسط کاربر شما در بازه زمانی ده ثانیه اخیر ارسال شده است. |
    | InvalidMarketPair | رمزارز مبدا (srcCurrency) یا رمزارز مقصد (dstCurrency) به درستی مقداردهی نشده
    است یا چنین بازاری در نوبیتکس وجود ندارد. |
    | MarketClosed | بازار مد نظر در حال حاضر به صورت موقت بسته است. |
    | TradingUnavailable | کاربر اجازه‌ی معامله ندارد، فرآیند احراز هویت خود را تکمیل نمایید. |
    | FeatureUnavailable | شما از کاربران مجاز به استفاده از امکانات آزمایشی نیستید. |

    ### نکات و ملاحظات

    1.  **محدودیت فراخوانی:** ۱۰۰ درخواست در هر ۱۰ دقیقه
    2.  **واحدها:** واحد قیمت در بازارهای ریالی به ریال (و نه تومان) می‌باشد. واحد قیمت در بازارهای تتری
    نیز تتر می‌باشد. واحد پارامتر مقدار (amount) بر حسب رمزارز مبدا (srcCurrency) است.
    3.  **تعیین محدوده مورد انتظار قیمت:** در سفارش‌های مارکت به شدت توصیه می‌شود که پارامتر price را
    نیز مشخص نمایید. این پارامتر در سفارش مارکت تخمین شما از قیمت بازار را نمایش می‌دهد و باعث می‌شود
    سفارش شما تنها تا جایی پر شود که قیمت معامله در بازه‌ی قیمتی مشخص شده باشد. برای پیش‌گیری از معاملات
    با قیمت ناخواسته به علت نوسانات دفعی بازار، پیشنهاد می‌شود که حتماً قیمت تقریبی مد نظر خود را در
    سفارش‌های مارکت نیز ارسال کنید. اگر پارامتر price را ارسال ننمایید، معامله با قیمت لحظه‌ای بازار (یا
    قیمت توقف در سفارش‌های حد ضرر) تا بازه نوسان ۱٪، انجام خواهد شد.
    4.  **سفارش تکراری:** برای جلوگیری از ثبت سفارش تکراری ناشی از اختلالات شبکه و سرور، در صورتی که دو
    سفارش با پارامترهای ورودی کاملاً مشابه از جمله نوع و قیمت و مقدار، در بازه‌ی زمانی کمتر از ده ثانیه
    ارسال نمایید، تنها سفارش اول پذیرفته می‌شود. (غیرفعال در حالت Pro)
    5.  **دقت مقادیر پولی (monetary):** نوع monetary که در ارامترهای `amount` و `price` به کار می‌رود،
    بسته به بازار هر رمزارز، تعداد رقم اعشار متغیری بین ۰ تا ۸ رقم دارد. در صورت ارسال مقادیر با ارقام
    اعشاری بیشتر، ارقام بی‌معنی
        در مقدار به پایین و در قیمت به روش بانکداری گرد خواهند شد.
        [مشاهده جدول دقت‌ها](https://nobitex.ir/policies/markets/)

    Args:
        body (PostMarketOrdersAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostMarketOrdersAddResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
