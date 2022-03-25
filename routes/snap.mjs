import { dirname } from "path";
import { fileURLToPath } from "url";
const __dirname = dirname(fileURLToPath(import.meta.url));

export default async (fastify, options) => {
  fastify.get("/", function (req, reply) {
    return reply.sendFile("snap.html", __dirname);
  });
};
