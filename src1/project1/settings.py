"""
Django settings for project1 project.

Generated by 'django-admin startproject' using Django 3.2.14.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

from .settings_secrets import SECRET_KEY, ALLOWED_HOSTS
#    -----------------        -------------------------
#    1                        2
# 1. `src1/project1/settings_secrets.py` を指しています
#                   ----------------
# 2. このファイル内では使われていませんが、このファイルを使う側から使われます

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#                        ------------------------
#                        1
# 1. 例えば `src1/project1/settings.py` ファイルから見て
#    .resolve()               は `code/projectN/settings.py` （`src1` は見えず `code` に差し変わっている）
#    .resolve().parent        は `code/projectN/`
#    .resolve().parent.parent は `code/`
#    となっていて、つまり BASE_DIR は あなたの開発用ディレクトリーを指している

# プロジェクト名を親ディレクトリー名から取得
PROJECT_NAME = os.path.basename(Path(__file__).resolve().parent)
# print(f"[projectN settings.py] PROJECT_NAME:{PROJECT_NAME}")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Application definition

INSTALLED_APPS = [
    # Djangoの標準アプリケーション
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # vvvv 追加 ここから
    # あなたが追加したアプリケーション
    # [O3o1o0g6o0] ワラベンチャー1.0巻
    'apps1.warabenture_vol1o0',
    # ^^^^ 追加 ここまで
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# * 変更前
# ROOT_URLCONF = 'project1.urls'
# * 変更後
ROOT_URLCONF = f'{PROJECT_NAME}.urls'
#                -------------------
#                1
# 1. DjangoのURL設定の大元となるPythonモジュール。
#    `src1/projectN/urls.py` を指している
#          -------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # * [O3o1o0g8o0] 変更前
        # 'DIRS': [],
        # * 変更後
        'DIRS': [
            # [O3o1o0g8o0] 練習1.0巻
            os.path.join(BASE_DIR, 'apps1/warabenture_vol1o0/templates'),
            #                       ----------------------------------
            #                       10
            # Example: /src1/apps1/warabenture_vol1o0/templates/warabenture_vol1o0/hello/ver1o0.html
            #                      ------------------           ------------------
            #                      11                           2
            #                -----------------------------------
            #                10
            # 10. テンプレート ディレクトリーへのパス
            # 11. アプリケーション
            # 2. まるで `http://example.com/warabenture_vol1o0` という素材フォルダーがあるかのように扱われる
            #                             -------------------
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# * 変更前
# WSGI_APPLICATION = 'project1.wsgi.application'
# * O2o1o0g9o1o2o_9o0 プロジェクト名の一般化
WSGI_APPLICATION = f'{PROJECT_NAME}.wsgi.application'
#                    -------------------------------
#                    1
# 1. DjangoのWSGI設定の大元となるグローバル変数。
#    `src1/projectN/wsgi.py` ファイルの中の application 変数を指している
#          -------------

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# * 変更前
# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
# }
# * 変更後
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
