import { dirname } from "path";
import { fileURLToPath } from "url";
const __dirname = dirname(fileURLToPath(import.meta.url));

export default async (fastify, options) => {
  fastify.get("/hud", function (req, reply) {
    return reply.send("this is the hud");
  });
};
