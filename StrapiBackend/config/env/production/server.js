// path: ./config/env/production/server.js

module.exports = ({ env }) => ({
  host: env("HOST", "0.0.0.0"),
  port: env.int("PORT", 1337),
  url: "https://agilestrapionazure.azurewebsites.net",
  admin: {
    url: "https://green-coast-007a37c03.2.azurestaticapps.net",
    serveAdminPanel: false,
  },
});
