import { useState } from 'react';
import axios from 'axios';

export default function UploadForm() {
  const [file, setFile] = useState(null);
  const [analysis, setAnalysis] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      alert("Selecione uma imagem!");
      return;
    }
    const formData = new FormData();
    formData.append('image', file);

    try {
      const uploadRes = await axios.post('http://localhost:5000/upload', formData);
      setAnalysis(uploadRes.data);
      setError(null);
    } catch (err) {
      setError(err.response?.data?.message || 'Erro ao enviar/redigir análise');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="file" accept="image/*" onChange={e => setFile(e.target.files[0])} />
      <button type="submit">Enviar e Analisar</button>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      {analysis && (
        <div>
          <h2>Nota: {analysis.nota_total}/1000</h2>
          <ul>
            {analysis.comentarios_por_competencia.map((c, i) => (
              <li key={i}>{c}</li>
            ))}
          </ul>
          <p><strong>Sugestões:</strong> {analysis.sugestoes_melhoria}</p>
        </div>
      )}
    </form>
  );
}

