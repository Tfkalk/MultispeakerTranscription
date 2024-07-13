# MultispeakerTranscription
Script to do multispeaker transcription with immediate transcript deletion.

## How do I use this?
Currently this uses AssemblyAI on the backend. Sign up for a free (up to 100 hours) account [here](https://www.assemblyai.com/dashboard/signup) and get your API key. The script will check for the API key value at $MULTISPEAKER_API. I recommend setting the value in your shell's config file. For those not comfortable in the shell, see below. The script will check that the value is set and exit if not.

You'll need to run `pip3 install assemblyai` (should work for macOS users) or `pip install assemblyai`, as applicable until I automate this.

When running MultispeakerTranscription, it currently expects to have an `Interviews` directory and a `Transcripts` directory in the same directory where it is being run. For example, if you have downloaded this file to `~/Downloads`, there should be `~/Downloads/Interviews` and `~/Downloads/Transcripts`. Then you can run this with `python3 MultiSpeakerTranscriber.py <filename>`. You only need to provide the file name. 

### What is this $SHELL
*Note: This guide is currently Unix-centric*

Python scripts are run from the command line (on macOS, this can be done with the bulit-in Terminal application). You are probably running the zsh shell, but to know for sure you can run `basename $SHELL`.

To set an environment variable, you can run `export <ENV_VAR_NAME>=<ENV_VAR_VALUE>`. However, this only lasts until you close the window or application. To persist the value, put that line in your shell's config file. For bash, this would be `~/.bash_profile` and for zsh, it would be `~/.zshrc`. For the change to take effect, either open a new window or run `source <that file>`. The config file gets run every time you start a new shell session.

I aim to make this friendly for non-tech people. If you have suggestions around how to improve either documentation or the script to make the barrier to entry lower, please cut a pull request.

## Data Protection
I built this for my journalism needs. The audio files include people who spoke to me on background or off the record so confidentiality was a tenet of design. This script uses AssemblyAI which [deletes](https://www.assemblyai.com/docs/concepts/faq) the audio file once transcription is complete. This script then immediately deletes the transcript from their server so the only copy that exists is the local one generated.
