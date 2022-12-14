/****************************************************************************
**
** Copyright (C) 2016 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of Qt for Python.
**
** $QT_BEGIN_LICENSE:LGPL$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see https://www.qt.io/terms-conditions. For further
** information use the contact form at https://www.qt.io/contact-us.
**
** GNU Lesser General Public License Usage
** Alternatively, this file may be used under the terms of the GNU Lesser
** General Public License version 3 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPL3 included in the
** packaging of this file. Please review the following information to
** ensure the GNU Lesser General Public License version 3 requirements
** will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 2.0 or (at your option) the GNU General
** Public license version 3 or any later version approved by the KDE Free
** Qt Foundation. The licenses are as published by the Free Software
** Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
** included in the packaging of this file. Please review the following
** information to ensure the GNU General Public License requirements will
** be met: https://www.gnu.org/licenses/gpl-2.0.html and
** https://www.gnu.org/licenses/gpl-3.0.html.
**
** $QT_END_LICENSE$
**
****************************************************************************/

#ifndef DYNAMICQMETAOBJECT_H
#define DYNAMICQMETAOBJECT_H

#include <sbkpython.h>
#include <pysidemacros.h>

#include <QtCore/QMetaObject>
#include <QtCore/QMetaMethod>

class MetaObjectBuilderPrivate;

namespace PySide
{

class MetaObjectBuilder
{
    Q_DISABLE_COPY(MetaObjectBuilder)
public:
    using EnumValue = QPair<QByteArray, int>;
    using EnumValues = QList<EnumValue>;

    MetaObjectBuilder(const char *className, const QMetaObject *metaObject);

    MetaObjectBuilder(PyTypeObject *type, const QMetaObject *metaObject);
    ~MetaObjectBuilder();

    int indexOfMethod(QMetaMethod::MethodType mtype, const QByteArray &signature) const;
    int indexOfProperty(const QByteArray &name) const;
    int addSlot(const char *signature);
    int addSlot(const char *signature, const char *type);
    int addSignal(const char *signature);
    void removeMethod(QMetaMethod::MethodType mtype, int index);
    int addProperty(const char *property, PyObject *data);
    void addInfo(const char *key, const char *value);
    void addInfo(const QMap<QByteArray, QByteArray> &info);
    void addEnumerator(const char *name, bool flag,
                       bool scoped, const EnumValues &entries);
    void removeProperty(int index);

    const QMetaObject *update();

    PYSIDE_API static QString formatMetaObject(const QMetaObject *metaObject);

private:
    MetaObjectBuilderPrivate *m_d;
};

}
#endif
