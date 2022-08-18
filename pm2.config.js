const WORKDIR = process.env.WORKDIR
const UID = process.env.PUID
const GID = process.env.PGID


module.exports = {
  apps : [
    {
      "name": "nastools",
      "script": "bash",
      "uid": UID,
      "gid": GID,
      "args": [
          "-c",
          "python3 run.py"
      ],
      "cwd": WORKDIR
    }
]
}
