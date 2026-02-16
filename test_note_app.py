from note_taking_app import load_notes, save_notes, add_note, edit_note, delete_note, list_notes # type: ignore

# Use a temporary filename to avoid clobbering the user's notes.json
import os
import json

# Backup existing notes.json if present
BACKUP = None
if os.path.exists('notes.json'):
    with open('notes.json', 'r', encoding='utf-8') as f:
        BACKUP = f.read()

# Start with empty notes
notes = []

print('Initial notes:', notes)

# Add notes
add_note(notes, 'First note')
add_note(notes, 'Second note')
print('After adding:', notes)

# Edit second note
edit_note(notes, 1, 'Second note - edited')
print('After editing:', notes)

# Delete first note
removed = delete_note(notes, 0)
print('Removed:', removed)
print('After deletion:', notes)

# Save to file and reload
save_notes(notes)
reloaded = load_notes()
print('Reloaded from file:', reloaded)

# Restore backup
if BACKUP is not None:
    with open('notes.json', 'w', encoding='utf-8') as f:
        f.write(BACKUP)
else:
    try:
        os.remove('notes.json')
    except OSError:
        pass

print('Test completed.')
