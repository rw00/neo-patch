package app.neo.patches.neo

import app.morphe.patcher.Fingerprint
import app.morphe.patcher.methodCall
import app.morphe.patcher.string

/** Identifies the Developer options check without matching the separate USB debugging check. */
object DevelopmentModeCheckFingerprint : Fingerprint(
    definingClass = "Lcom/xamdesign/safe_device/DevelopmentMode/DevelopmentModeCheck;",
    name = "developmentModeCheck",
    isStatic = true,
    returnType = "Z",
    parameters = listOf("Landroid/content/Context;"),
    filters = listOf(
        string("development_settings_enabled"),
        methodCall(
            smali = "Landroid/provider/Settings\$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I"
        )
    )
)
