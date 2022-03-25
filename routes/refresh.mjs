import { dirname } from "path";
import { process } from "../display-scripts/process.mjs";

import { fileURLToPath } from "url";
const __dirname = dirname(fileURLToPath(import.meta.url));

// this is to clear the screen
export default async (fastify, options) => {
  fastify.get("/clear", function (req, reply) {
    // spin off a process to clear
    process("python ./display-scripts/stripes.py");
    return reply.send("this is to clear the screen");
  });

  fastify.get("/cycle", function (req, reply) {
    // spin off a process to clear
    process("python ./display-scripts/cycle.py");
    return reply.send("this is to clear the screen");
  });

  fastify.get("/stripes", function (req, reply) {
    // spin off a process to clear
    process("python ./display-scripts/stripes.py");
    return reply.send("this outputs all the colors to the screen");
  });
};
