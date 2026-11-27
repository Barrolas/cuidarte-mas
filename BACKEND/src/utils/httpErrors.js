/**
 * Respuesta estándar para errores internos (HTTP 500) - INC-06
 * Registra el error real solo en el log del servidor y responde al cliente
 * con el formato { error, glosa } sin exponer detalles internos (SQL, stack).
 */
const GLOSA_ERROR_INTERNO = "Ocurrió un error interno en el servidor";

function sendInternalError(res, err, error, glosa = GLOSA_ERROR_INTERNO) {
  console.error(err);
  return res.status(500).json({ error, glosa });
}

module.exports = {
  GLOSA_ERROR_INTERNO,
  sendInternalError,
};
