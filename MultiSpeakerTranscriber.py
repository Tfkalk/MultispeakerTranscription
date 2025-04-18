import assemblyai as aai
import os
import sys
import argparse
from decimal import Decimal

# Methods
def transcribe_file(path, file):
	# Chop off extension from file
	filename = os.path.splitext(file)[0]
	
	try:
		f = open(filename + ".txt", "x")
	except FileExistsError:
		print("A transcript with this name already exists. Please delete that transcript or provide a different file.")
		sys.exit(4)
	

	# Transcribe the audio.
	aai.settings.api_key = API_KEY
	config = aai.TranscriptionConfig(speaker_labels=True)

	transcriber = aai.Transcriber()

	print("Proceeding to transcribe the file: " + file)
	
	transcript = transcriber.transcribe(
		os.path.join(path, file),
		config=config
	)

	if transcript.status == aai.TranscriptStatus.error:
		print(f"Transcription failed: {transcript.error}")

	# Write to the file.
	print("Generating file.")
	for utterance in transcript.utterances:
	  seconds = Decimal(utterance.start) / 1000
	  f.write(f"Speaker {utterance.speaker} @{seconds}sec: {utterance.text}\n")

	f.close()

	# Delete the transcript so the only copy is local.
	print("Proceeding to delete transcript id: " + transcript.id)
	transcript.delete_by_id(transcript.id)

API_KEY = os.getenv("MULTISPEAKER_API")
if API_KEY is None:
	print("You are missing a value at $ASSEMBLY_AI_API. Set your API key and run again")
	sys.exit(3)
	
# Take in an argument of the file
parser = argparse.ArgumentParser("MultispeakerTranscribe")
parser.add_argument("--file", dest='audio', help="The path of the audio file to be transcribed.")
parser.add_argument("--batch", dest='directory', help="A directory of files to transcribe. All files will be submitted for transcription.")
args = parser.parse_args()

if args.audio is not None:
	transcribe_file(".", args.audio)
	
if args.directory is not None:
	path = args.directory

	if os.path.isdir(path) is False:
		print("Must provide a directory to use with the batch flag.")
		sys.exit(5)

	# Iterate through the files.
	onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
	print("Proceeding to process files in " + path)
	for file in onlyfiles:
		if file != ".DS_Store":
			transcribe_file(path, file)
	
