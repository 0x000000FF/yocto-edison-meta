#!/usr/bin/env python
# coding: utf-8
'''
定义可以将按钮(button)用于 Flask 表单(form)的域(field)
提供 button式 和 input type='button'式 两种
'''

from werkzeug.utils import escape, text_type
from wtforms import BooleanField, Field, Label
from wtforms.widgets.core import HTMLString, TextInput, Input, html_params

__author__ = 'Jux.Liu'


class ButtonInput(Input):
    """
    用于显示 input type='button' 式按钮的部件(widget)
    """
    input_type = 'button'

    def __call__(self, field, **kwargs):
        kwargs.setdefault('value', field.label.text)
        return super(ButtonInput, self).__call__(field, **kwargs)


class ButtonInputField(BooleanField):
    '''
    input type='button'式按钮
    '''
    widget = ButtonInput()


class ButtonWidget(object):
    '''
    用于显示 button 式按钮的部件(widget)
    '''

    def __call__(self, field, **kwargs):
        if field.name is not None:
            kwargs.setdefault('name', field.name)
        if field.value is not None:
            kwargs.setdefault('value', field.value)
        kwargs.setdefault('type', field.type)
        kwargs.setdefault('id', field.id)
        return HTMLString('<button %s>%s</button>' % (html_params(**kwargs), escape(field._value())))


class ButtonButtonField(Field):
    '''
    button式按钮
    '''
    widget = ButtonWidget()

    def __init__(self, bid=None, text=None, name=None, value=None, btype='button', label=None, **kwargs):
        """
        button式按钮构造函数
        :param bid: 按钮id——只在不使用 wtf.quick_form()时生效
        :param text: 按钮显示的文本
        :param name: 按钮的名称
        :param value: 按钮的初始值
        :param btype: submit/button/reset.
        :param label: 按钮前置Label——只在使用wtf.quick_form()时生效或使用 .label 方式强制
        """
        super(ButtonButtonField, self).__init__(**kwargs)
        if label is None:
            self.label = Label(field_id='Null', text='')
        else:
            self.label = Label(field_id=self.short_name, text=label)
        self.text = text
        self.value = value
        self.type = btype
        self.id = bid
        if name is not None:
            self.name = name

    def _value(self):
        return text_type(self.text)


class DisabledTextInput(TextInput):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('type', self.input_type)
        if 'value' not in kwargs:
            kwargs['value'] = field._value()
        return HTMLString(u'<input type="text" disabled="disabled" />'
                          % self.html_params(name=field.name, **kwargs))
