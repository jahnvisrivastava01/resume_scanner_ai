import { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [role, setRole] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const roles = [
    "frontend developer",
    "backend developer",
    "full stack developer",
    "python developer",
    "java developer",
    "data analyst",
    "machine learning engineer",
    "ui ux designer",
    "android developer",
    "software tester",
    "devops engineer",
    "general fresher"
  ];

  const handleSubmit = async () => {
    if (!file || !role) {
      alert("Please upload resume and select role");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("role", role);

    try {
      setLoading(true);

      const res = await axios.post(
        "http://127.0.0.1:8000/analyze",
        formData
      );

      setResult(res.data);
    } catch (error) {
      console.log(error);
      alert("Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-white px-4 py-10">
      <div className="max-w-4xl mx-auto">

        {/* Header */}
        <div className="text-center mb-10">
          <h1 className="text-4xl md:text-5xl font-bold bg-gradient-to-r from-blue-400 to-cyan-300 bg-clip-text text-transparent">
            Resume Scanner AI
          </h1>
          <p className="text-slate-400 mt-3 text-lg">
            Upload your resume and check your role readiness
          </p>
        </div>

        {/* Main Card */}
        <div className="bg-slate-900 border border-slate-800 rounded-3xl shadow-2xl p-6 md:p-8 space-y-5">

          {/* Upload */}
          <div>
            <label className="block mb-2 text-sm text-slate-300">
              Upload Resume
            </label>
            <input
              type="file"
              onChange={(e) => setFile(e.target.files[0])}
              className="w-full bg-slate-800 border border-slate-700 rounded-xl p-3 file:mr-4 file:px-4 file:py-2 file:rounded-lg file:border-0 file:bg-blue-600 file:text-white hover:file:bg-blue-700"
            />
          </div>

          {/* Role Select */}
          <div>
            <label className="block mb-2 text-sm text-slate-300">
              Select Target Role
            </label>
            <select
              onChange={(e) => setRole(e.target.value)}
              className="w-full bg-slate-800 border border-slate-700 rounded-xl p-3 text-white outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="">Choose Role</option>
              {roles.map((item, index) => (
                <option key={index} value={item}>
                  {item}
                </option>
              ))}
            </select>
          </div>

          {/* Button */}
          <button
            onClick={handleSubmit}
            className="w-full bg-gradient-to-r from-blue-600 to-cyan-500 hover:opacity-90 transition-all duration-300 rounded-xl py-3 text-lg font-semibold"
          >
            {loading ? "Analyzing..." : "Analyze Resume"}
          </button>
        </div>

        {/* Result Section */}
        {result && (
          <div className="mt-8 bg-slate-900 border border-slate-800 rounded-3xl shadow-2xl p-6 md:p-8">

            <h2 className="text-2xl font-bold mb-6 text-cyan-300">
              Analysis Result
            </h2>

            {/* Score */}
            <div className="grid md:grid-cols-2 gap-6">

              <div className="bg-slate-800 rounded-2xl p-5">
                <p className="text-slate-400 text-sm">Target Role</p>
                <h3 className="text-xl font-semibold capitalize mt-1">
                  {result.role}
                </h3>

                <p className="text-slate-400 text-sm mt-5">Match Score</p>
                <div className="text-5xl font-bold text-green-400 mt-2">
                  {result.match_score}%
                </div>
              </div>

              <div className="bg-slate-800 rounded-2xl p-5">
                <p className="text-slate-400 text-sm mb-3">
                  Suggestion
                </p>
                <p className="leading-7 text-slate-200">
                  {result.suggestion}
                </p>
              </div>
            </div>

            {/* Skills */}
            <div className="grid md:grid-cols-2 gap-6 mt-6">

              {/* Found Skills */}
              <div className="bg-slate-800 rounded-2xl p-5">
                <h3 className="text-lg font-semibold text-green-400 mb-3">
                  Found Skills
                </h3>

                <div className="flex flex-wrap gap-2">
                  {result.found_skills.map((skill, i) => (
                    <span
                      key={i}
                      className="px-3 py-1 rounded-full bg-green-500/20 text-green-300 text-sm"
                    >
                      {skill}
                    </span>
                  ))}
                </div>
              </div>

              {/* Missing Skills */}
              <div className="bg-slate-800 rounded-2xl p-5">
                <h3 className="text-lg font-semibold text-red-400 mb-3">
                  Missing Skills
                </h3>

                <div className="flex flex-wrap gap-2">
                  {result.missing_skills.map((skill, i) => (
                    <span
                      key={i}
                      className="px-3 py-1 rounded-full bg-red-500/20 text-red-300 text-sm"
                    >
                      {skill}
                    </span>
                  ))}
                </div>
              </div>
            </div>

          </div>
        )}
      </div>
    </div>
  );
}

export default App;