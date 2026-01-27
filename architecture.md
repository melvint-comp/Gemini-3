# KC-IDS Architecture

```markdown
## Step 1: Cloud Telemetry Collection
KC-IDS consumes Google Cloud logs including IAM, KMS, API calls, and network flows.

## Step 2: Event Streaming
Logs are streamed via Pub/Sub to enable near real-time processing.

## Step 3: Feature Engineering
Access behavior is transformed into features:
- Identity vs key ownership
- Temporal patterns
- Location & network context

## Step 4: Detection Engine
A neural network performs classification and anomaly detection.
A reinforcement learning agent tunes decision thresholds over time.

## Step 5: Gemini 3 Reasoning
Gemini 3 interprets events and generates:
- Incident explanations
- Contextual summaries
- Human-readable insights

## Step 6: Synthetic Data Generation
Gemini 3 creates realistic fraud scenarios to strengthen training.

## Step 7: Evaluation & Feedback
Model performance is analyzed after each cycle.

## Step 8: Kaizen MLOps Loop
Vertex AI pipelines retrain and redeploy models automatically.

The system never stops learning.
