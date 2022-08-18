const WORKDIR = process.env.WORKDIR


module.exports = {
  apps : [
    {
      "name": "nastools",
      "script": "bash",
      "args": [
          "-c",
          "python3 run.py"
      ],
      "cwd": WORKDIR
    }
]
}
