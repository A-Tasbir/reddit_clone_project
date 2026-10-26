#!/usr/bin/env python3
from pathlib import Path

root = Path("PocketLedger")
gradle = root / "app/build.gradle.kts"
manifest = root / "app/src/main/AndroidManifest.xml"
main = root / "app/src/main/java/com/example/pocketledger/MainActivity.kt"
backup = root / "app/src/main/java/com/example/pocketledger/BackupManager.kt"

def replace_once(file, old, new):
    value = file.read_text()
    assert value.count(old) == 1, f"{file}: expected exactly one {old!r}"
    file.write_text(value.replace(old, new))

original_backup = backup.read_bytes()
assert b'const val BACKUP_VERSION = 1' in original_backup
assert b'"pocketledger-backup"' in original_backup
replace_once(gradle, 'applicationId = "com.example.pocketledger"', 'applicationId = "com.example.pocketledger.next"')
replace_once(gradle, 'versionCode = 1', 'versionCode = 2')
replace_once(gradle, 'versionName = "0.1.0"', 'versionName = "0.2.0"')
replace_once(manifest, 'android:label="PocketLedger"', 'android:label="PocketLedger Next"')
replace_once(main, 'Text("PocketLedger", fontWeight = FontWeight.Bold, letterSpacing = 0.2.sp)', 'Text("PocketLedger Next", fontWeight = FontWeight.Bold, letterSpacing = 0.2.sp)')
replace_once(main, 'Text("Your money, in your hands", fontSize = 11.sp, color = muted)', 'Text("v0.2 · independent app", fontSize = 11.sp, color = muted)')
replace_once(main, 'export.launch("PocketLedger-$date.json")', 'export.launch("PocketLedger-Next-$date.json")')
replace_once(main, 'Text("Restore from backup file")', 'Text("Import backup (v0.1 compatible)")')
replace_once(main, 'SectionHeader("Keep your data safe")', """SectionHeader("Keep your data safe")
        Card(colors = CardDefaults.cardColors(containerColor = panelSecondary), shape = RoundedCornerShape(16.dp)) {
            Column(Modifier.padding(16.dp), verticalArrangement = Arrangement.spacedBy(6.dp)) {
                Text("Bring your data from PocketLedger v0.1", fontWeight = FontWeight.Bold, color = accent)
                Text("1. Open PocketLedger v0.1 > Backup > Export backup file. Save the .json file to Downloads or Documents.", color = lightText, fontSize = 13.sp)
                Text("2. In PocketLedger Next, tap Import backup below and select the exported .json file.", color = lightText, fontSize = 13.sp)
                Text("3. Review the account and transaction counts and confirm. Import replaces only this app's data. Your v0.1 data is never touched.", color = muted, fontSize = 13.sp)
            }
        }""")
assert backup.read_bytes() == original_backup, "The v0.1 backup codec must stay compatible"
print("Prepared separate PocketLedger Next package with unchanged v0.1 backup codec.")
