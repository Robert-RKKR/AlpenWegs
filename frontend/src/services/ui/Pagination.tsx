type Props = {
  page: number;
  pageCount: number;
  onChange: (page: number) => void;
};

export function Pagination({
  page,
  pageCount,
  onChange,
}: Props) {
  return (
    <div style={{ marginTop: 16 }}>
      <button
        disabled={page === 1}
        onClick={() => onChange(page - 1)}
      >
        Previous
      </button>

      <span style={{ margin: "0 8px" }}>
        Page {page} of {pageCount}
      </span>

      <button
        disabled={page === pageCount}
        onClick={() => onChange(page + 1)}
      >
        Next
      </button>
    </div>
  );
}
