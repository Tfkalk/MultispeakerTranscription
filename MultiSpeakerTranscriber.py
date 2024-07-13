import assemblyai as aai
import os
import sys
import argparse

API_KEY = os.getenv("MULTISPEAKER_API")
if API_KEY is None:
	print("You are missing a value at $ASSEMBLY_AI_API. Set your API key and run again")
	sys.exit(3)
	
# Take in an argument of the file
parser = argparse.ArgumentParser("MultispeakerTranscribe")
parser.add_argument("audio", help="The filename of an audio file to be transcribed.")
args = parser.parse_args()

# Chop off extension from file
file = args.audio
filename = os.path.splitext(file)[0]

try:
	f = open("./Transcripts/" + filename + ".txt", "x")
except FileExistsError:
	print("A transcript with this name already exists. Please delete that transcript or provide a different file.")
	sys.exit(4)
	

# Transcribe the audio.
aai.settings.api_key = API_KEY
config = aai.TranscriptionConfig(speaker_labels=True)

transcriber = aai.Transcriber()

print("Proceeding to transcribe the file.")

transcript = transcriber.transcribe(
	"./Interviews/"+file,
	config=config
)


# Write to the file.
print("Generating file.")
for utterance in transcript.utterances:
  f.write(f"Speaker {utterance.speaker}: {utterance.text}\n")

f.close()

# Delete the transcript so the only copy is local.
print("Proceeding to transcript id: " + transcript.id)
transcript.delete_by_id(transcript.id)
