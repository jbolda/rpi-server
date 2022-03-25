import { join, dirname } from "path";
import AutoLoad from "fastify-autoload";
import { fileURLToPath } from "url";
const __dirname = dirname(fileURLToPath(import.meta.url));

export default async function (fastify, opts) {
  // Place here your custom code!
  fastify.register(import("fastify-static"), {
    root: join(__dirname, "public"),
    prefix: "/public/", // optional: default '/'
  });

  // This loads all plugins defined in plugins
  // those should be support plugins that are reused
  // through your application
  fastify.register(AutoLoad, {
    dir: join(__dirname, "plugins"),
    options: Object.assign({}, opts),
  });

  // This loads all plugins defined in routes
  // define your routes in one of these
  fastify.register(AutoLoad, {
    dir: join(__dirname, "routes"),
    options: Object.assign({}, opts),
  });
}
