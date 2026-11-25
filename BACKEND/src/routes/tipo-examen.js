const express = require("express");
const { pool } = require("../db");
const { sendInternalError } = require("../utils/httpErrors");
const router = express.Router();

// Listar tipos de examen (público para autenticados)
router.get("/", async (req, res) => {
  try {
    const result = await pool.query(
      "SELECT * FROM tipo_examen_medico ORDER BY nombre ASC"
    );
    res.json(result.rows);
  } catch (err) {
    sendInternalError(res, err, "Error al listar tipos de examen");
  }
});

// Obtener tipo de examen por ID
router.get("/:id", async (req, res) => {
  try {
    const result = await pool.query(
      "SELECT * FROM tipo_examen_medico WHERE id = $1",
      [req.params.id]
    );

    if (result.rows.length === 0)
      return res.status(404).json({ error: "No encontrado" });

    res.json(result.rows[0]);
  } catch (err) {
    sendInternalError(res, err, "Error al obtener tipo de examen");
  }
});

module.exports = router;

