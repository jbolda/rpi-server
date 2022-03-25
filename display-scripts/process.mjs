import { run, spawn } from "effection";
import { exec } from "@effection/process";

export const process = (command) =>
  run(function* () {
    let childProcess = yield exec(command);

    yield spawn(
      childProcess.stdout.forEach((text) => console.log(text.toString().trim()))
    );
    yield spawn(
      childProcess.stderr.forEach((text) =>
        console.error(text.toString().trim())
      )
    );

    let result = yield childProcess.join();
    console.log(result);
  });
