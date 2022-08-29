/****************************************************************************
**
** Copyright (C) 2021 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of Qt Quick 3D.
**
** $QT_BEGIN_LICENSE:GPL$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see https://www.qt.io/terms-conditions. For further
** information use the contact form at https://www.qt.io/contact-us.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 3 or (at your option) any later version
** approved by the KDE Free Qt Foundation. The licenses are as published by
** the Free Software Foundation and appearing in the file LICENSE.GPL3
** included in the packaging of this file. Please review the following
** information to ensure the GNU General Public License requirements will
** be met: https://www.gnu.org/licenses/gpl-3.0.html.
**
** $QT_END_LICENSE$
**
****************************************************************************/

import QtQuick 2.15
import QtQuick.Layouts 1.15
import HelperWidgets 2.0
import StudioTheme 1.0 as StudioTheme

Section {
    caption: qsTr("Particle Affector")
    width: parent.width

    SectionLayout {
        PropertyLabel {
            text: qsTr("System")
            tooltip: qsTr("This property defines the ParticleSystem3D for the affector. If system is direct parent of the affector, this property does not need to be defined.")
        }

        SecondColumnLayout {
            IdComboBox {
                typeFilter: "QtQuick3D.Particles3D.ParticleSystem3D"
                backendValue: backendValues.system
                implicitWidth: StudioTheme.Values.singleControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Particles")
            tooltip: qsTr("This list controls which logical particles will be affected. When empty, all particles in the system are affected.")
            Layout.alignment: Qt.AlignTop
            Layout.topMargin: 5
        }

        SecondColumnLayout {
            EditableListView {
                backendValue: backendValues.particles
                model: backendValues.particles.expressionAsList
                Layout.fillWidth: true
                typeFilter: "QtQuick3D.Particles3D.Particle3D"

                onAdd: function(value) { backendValues.particles.idListAdd(value) }
                onRemove: function(idx) { backendValues.particles.idListRemove(idx) }
                onReplace: function (idx, value) { backendValues.particles.idListReplace(idx, value) }
            }

            ExpandingSpacer {}
        }

        PropertyLabel {
            text: qsTr("Enabled")
            tooltip: qsTr("If enabled is set to false, this affector will not alter any particles. Usually this is used to conditionally turn an affector on or off.")
        }

        SecondColumnLayout {
            CheckBox {
                id: enabledCheckBox
                text: backendValues.enabled.valueToString
                backendValue: backendValues.enabled
                implicitWidth: StudioTheme.Values.twoControlColumnWidth
                               + StudioTheme.Values.actionIndicatorWidth
            }

            ExpandingSpacer {}
        }
    }
}
