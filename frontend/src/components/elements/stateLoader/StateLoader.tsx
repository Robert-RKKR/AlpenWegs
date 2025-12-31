// Import component css:
import "./StateLoader.css";

type StateLoaderProps = {
  size?: number;
  className?: string;
};

export function StateLoader({
  size = 32,
}: StateLoaderProps) {
  return (
    <div
      className="state-loader"
      style={{ width: size, height: size }}
    />
  );
}
